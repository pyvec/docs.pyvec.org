"""
Sphinx extension which adds a new role :slack:, which allows you to easily
make links to pyvec.slack.com Slack channels. Example::

    In any doubt, ask in the :slack:`#pyvo` channel.
"""

import functools

from docutils import nodes

from pyvec_docs.board import BOARD_HISTORY


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def slack(
    name,
    rawtext,
    text,
    lineno,
    inliner,
    options=None,
    content=None,
    pyvec_board_years=None,
):
    text = text.lstrip("#")

    if pyvec_board_years and text.startswith("pyvec-board"):
        text = f"pyvec-board-{pyvec_board_years[0]}-{pyvec_board_years[1]}"

    url = f"https://pyvec.slack.com/app_redirect?channel={text}"
    node = nodes.reference(rawtext, f"#{text}", refuri=url, **(options or {}))
    return [node], []


def setup(app):
    board_year_from = BOARD_HISTORY[0]["from"].year
    board_years = (board_year_from, board_year_from + 3)

    app.add_role("slack", functools.partial(slack, pyvec_board_years=board_years))
    return {"version": "1.0", "parallel_read_safe": True}
