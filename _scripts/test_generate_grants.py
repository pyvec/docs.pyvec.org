from datetime import date, datetime

import pytest
from generate_grants import get_board_member_name, get_votes, remove_comments, to_date


@pytest.fixture
def board_history():
    return [  # sorted!
        {
            "from": datetime(2020, 1, 1),
            "members": {"alice": "Alice", "doubravka": "Doubravka"},
        },
        {"from": datetime(2019, 1, 1), "members": {"bobby": "Bob"}},
    ]


def test_to_date():
    assert to_date("2020-02-12T13:22:01Z") == date(2020, 2, 12)


def test_remove_comments():
    assert (
        remove_comments(
            """
                <!-- hello -->
                something
                <!-- bye -->
            """
        )
        == "something"
    )


@pytest.mark.parametrize(
    "username,voted_at,expected",
    [
        pytest.param("bobby", date(2019, 8, 30), "Bob", id="bob-board-y"),
        pytest.param("alice", date(2019, 8, 30), None, id="alice-board-n"),
        pytest.param("bobby", date(2020, 8, 30), None, id="bob-board-n"),
        pytest.param("alice", date(2020, 8, 30), "Alice", id="alice-board-y"),
    ],
)
def test_get_board_member_name(username, voted_at, board_history, expected):
    assert get_board_member_name(username, voted_at, board_history) == expected


def test_get_votes_returns_only_board_members_votes(board_history):
    reactions = [
        {"user": {"login": "bobby"}, "content": "+1"},
        {"user": {"login": "alice"}, "content": "+1"},
        {"user": {"login": "doubravka"}, "content": "+1"},
    ]

    assert list(get_votes(reactions, date(2020, 8, 30), board_history)) == [
        {"name": "Alice", "text": "ano"},
        {"name": "Doubravka", "text": "ano"},
    ]


def test_get_votes_returns_only_relevant_emojis(board_history):
    reactions = [
        {"user": {"login": "alice"}, "content": "+1"},
        {"user": {"login": "doubravka"}, "content": "heart"},
    ]

    assert list(get_votes(reactions, date(2020, 8, 30), board_history)) == [
        {"name": "Alice", "text": "ano"},
    ]


@pytest.mark.parametrize(
    "content,expected",
    [
        ("+1", "ano"),
        ("-1", "ne"),
        ("eyes", "zdržel(a) se"),
    ],
)
def test_get_votes_understands_all_relevant_emojis(content, board_history, expected):
    reactions = [
        {"user": {"login": "alice"}, "content": content},
        {"user": {"login": "doubravka"}, "content": "heart"},
    ]

    assert list(get_votes(reactions, date(2020, 8, 30), board_history)) == [
        {"name": "Alice", "text": expected},
    ]
