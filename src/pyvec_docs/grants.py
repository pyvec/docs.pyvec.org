import re
from datetime import date

from pyvec_docs.boards import Board


REACTIONS_MAPPING = {"+1": "ano", "-1": "ne", "eyes": "zdržel(a) se"}


def to_date(iso_datetime_string):
    iso_date_string, _ = iso_datetime_string.split("T")
    return date.fromisoformat(iso_date_string)


def remove_comments(html):
    return re.sub(r"<!--[^<]+-->", "", html).strip()


def get_board_member_name(username, voted_at, boards: list[Board]):
    for board in boards:  # sorted from the most recent
        if voted_at > board.start_on:
            for member in board.members:
                if member.github == username:
                    return member.name
            return None
    return None


def get_votes(reactions, voted_at, boards: list[Board]):
    for reaction in reactions:
        username = reaction["user"]["login"]
        name = get_board_member_name(username, voted_at, boards)
        if name:  # else not reaction from a board member
            text = REACTIONS_MAPPING.get(reaction["content"])
            if text:
                yield {"name": name, "text": text}


def get_lock_date(events):
    for event in reversed(events):
        if event["event"] == "locked":
            return to_date(event["created_at"])
