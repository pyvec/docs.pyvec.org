import os
from operator import itemgetter
from pathlib import Path

import requests
from jinja2 import Template

from pyvec_docs.board import BOARD_HISTORY
from pyvec_docs.grants import get_lock_date, get_votes, remove_comments, to_date


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_API_HEADERS = {
    "Accept": "application/vnd.github.squirrel-girl-preview",
    "Authorization": f"token {GITHUB_TOKEN}",
}
GITHUB_API_URL = "https://api.github.com/repos/pyvec/money/issues"
CONTENT_PATH = Path(__file__).parent.parent


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
        votes = list(get_votes(res.json(), voted_at, BOARD_HISTORY))

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
