import pytest
from slack import slack


def test_slack():
    nodes, _ = slack('slack', ':slack:`#pyvo`', '#pyvo', None, None)

    assert nodes[0]['refuri'] == 'https://pyvec.slack.com/app_redirect?channel=pyvo'


@pytest.mark.parametrize('text, expected', [
    ("pyvo", "pyvo"),
    ("pyvec-board", "pyvec-board-2000-3000"),
    ("pyvec-board-", "pyvec-board-2000-3000"),
    ("pyvec-board-1987-4587", "pyvec-board-2000-3000"),
])
def test_slack_board(text, expected):
    nodes, _ = slack('slack', f':slack:`#{text}`', f'#{text}', None, None,
                     pyvec_board_years=(2000, 3000))

    assert nodes[0]['refuri'] == f'https://pyvec.slack.com/app_redirect?channel={expected}'
