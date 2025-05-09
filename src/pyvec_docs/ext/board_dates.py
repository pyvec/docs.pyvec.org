from datetime import timedelta
from typing import Any

from sphinx.application import Sphinx
from sphinx.config import Config

from pyvec_docs.board import BOARDS_MANDATE_LENGTH, load_boards


def board_dates(app: Sphinx, config: Config):
    board = load_boards()[0]

    board_start = board.start_on
    board_end = board_start + timedelta(days=BOARDS_MANDATE_LENGTH * 365)

    existing_epilog = app.config.rst_epilog or ""
    app.config.rst_epilog = (
        f"{existing_epilog}\n\n"
        f".. |board_start| replace:: {board_start:%-d.%-m.%Y}\n"
        f".. |board_end| replace:: {board_end:%Y}\n"
    )


def setup(app: Sphinx) -> dict[str, Any]:
    app.connect("config-inited", board_dates)
    return {"version": "1.0", "parallel_read_safe": True, "parallel_write_safe": True}
