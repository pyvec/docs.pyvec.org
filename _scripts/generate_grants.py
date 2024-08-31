import os
import re
from datetime import date
from operator import itemgetter
from pathlib import Path

import requests
import strictyaml as yaml
from jinja2 import Template


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_HEADERS = {
    "Accept": "application/vnd.github.squirrel-girl-preview",
    "Authorization": f"token {GITHUB_TOKEN}",
}
GITHUB_API_URL = "https://api.github.com/repos/pyvec/money/issues"
REACTIONS_MAPPING = {"+1": "ano", "-1": "ne", "eyes": "zdržel(a) se"}
CONTENT_PATH = Path(__file__).parent.parent

BOARD_HISTORY_SCHEMA = yaml.Seq(
    yaml.Map(
        {
            "from": yaml.Datetime(),
            "members": yaml.MapPattern(yaml.Str(), yaml.Str()),
        }
    )
)
BOARD_HISTORY_PATH = Path(__file__).parent.parent / "board.yml"
BOARD_HISTORY = sorted(
    yaml.load(BOARD_HISTORY_PATH.read_text(), BOARD_HISTORY_SCHEMA).data,
    key=itemgetter("from"),
    reverse=True,
)


def to_date(iso_datetime_string):
    iso_date_string, _ = iso_datetime_string.split("T")
    return date.fromisoformat(iso_date_string)


def remove_comments(html):
    return re.sub(r"<!--[^<]+-->", "", html).strip()


def get_board_member_name(username, voted_at, board_history=None):
    board_history = board_history or BOARD_HISTORY
    for board in board_history:  # sorted from the most recent
        if voted_at > board["from"].date():
            return board["members"].get(username)
    return None


def get_votes(reactions, voted_at, board_history=None):
    for reaction in reactions:
        username = reaction["user"]["login"]
        name = get_board_member_name(username, voted_at, board_history)
        if name:  # else not reaction from a board member
            text = REACTIONS_MAPPING.get(reaction["content"])
            if text:
                yield {"name": name, "text": text}


def get_lock_date(events):
    for event in reversed(events):
        if event["event"] == "locked":
            return to_date(event["created_at"])


if __name__ == "__main__":
    res = requests.get(
        GITHUB_API_URL,
        headers=GITHUB_API_HEADERS,
        params={"per_page": 100, "state": "closed"},
    )
    res.raise_for_status()

    grants = []
    for issue in res.json():
        labels = [label["name"] for label in issue["labels"]]
        if "approved" not in labels and "rejected" not in labels:
            # skip unlabeled, e.g. https://github.com/pyvec/money/issues/1
            continue

        if issue["locked"]:
            res = requests.get(
                issue["events_url"],
                headers=GITHUB_API_HEADERS,
                params={"per_page": 100},
            )
            res.raise_for_status()

            if res.headers.get("link"):
                raise NotImplementedError(
                    f"The number of events of issue #{issue['number']} "
                    "is paginated and this code isn't yet designed "
                    "to handle this!"
                )
            else:
                voted_at = get_lock_date(res.json())
        else:
            voted_at = to_date(issue["closed_at"])

        res = requests.get(issue["reactions"]["url"], headers=GITHUB_API_HEADERS)
        res.raise_for_status()
        votes = list(get_votes(res.json(), voted_at))

        grants.append(
            {
                "title": issue["title"],
                "description": remove_comments(issue["body"]),
                "url": issue["html_url"],
                "user": {
                    "username": issue["user"]["login"],
                    "url": issue["user"]["html_url"],
                },
                "is_approved": "approved" in labels,
                "filed_at": to_date(issue["created_at"]),
                "voted_at": voted_at,
                "votes": votes,
            }
        )
    grants = sorted(grants, key=itemgetter("voted_at"), reverse=True)

    tpl_path = CONTENT_PATH / "operations" / "grants.rst.jinja"
    tpl = Template(tpl_path.read_text())
    print(tpl.render(grants=grants))
