import re
from datetime import date


REACTIONS_MAPPING = {"+1": "ano", "-1": "ne", "eyes": "zdržel(a) se"}


def to_date(iso_datetime_string):
    iso_date_string, _ = iso_datetime_string.split("T")
    return date.fromisoformat(iso_date_string)


def remove_comments(html):
    return re.sub(r"<!--[^<]+-->", "", html).strip()


def get_board_member_name(username, voted_at, board_history):
    for board in board_history:  # sorted from the most recent
        if voted_at > board["from"].date():
            return board["members"].get(username)
    return None


def get_votes(reactions, voted_at, board_history):
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
