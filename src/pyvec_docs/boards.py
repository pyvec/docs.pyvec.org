import tomllib
from datetime import date
from enum import StrEnum
from functools import cache
from operator import attrgetter
from pathlib import Path

from pydantic import BaseModel


BOARDS_CONFIG_PATH = Path(__file__).parent / "boards.toml"

BOARDS_MANDATE_LENGTH = 3


class BoardRole(StrEnum):
    chair = "chair"
    treasurer = "treasurer"


class BoardMember(BaseModel):
    name: str
    github: str
    roles: set[BoardRole] | None = set()

    model_config = {"extra": "forbid", "frozen": True}

    @property
    def is_chair(self) -> bool:
        if self.roles is None:
            return False
        return BoardRole.chair in self.roles

    @property
    def is_treasurer(self) -> bool:
        if self.roles is None:
            return False
        return BoardRole.treasurer in self.roles


class Board(BaseModel):
    start_on: date
    voted_on: date
    has_started: bool
    members: list[BoardMember]

    model_config = {"extra": "forbid", "frozen": True}

    @classmethod
    def create(cls, voted_on=None, start_on=None, **kwargs):
        if start_on is None:
            start_on = voted_on
            has_started = False
        else:
            has_started = True
        return cls(
            voted_on=voted_on,
            start_on=start_on,
            has_started=has_started,
            **kwargs,
        )

    @property
    def years(self) -> tuple[int, int]:
        start_year = self.start_on.year
        return (start_year, start_year + BOARDS_MANDATE_LENGTH)


@cache
def load_boards(path: Path | str = BOARDS_CONFIG_PATH) -> list[Board]:
    """Load all boards, including inactive ones"""
    data = tomllib.loads(Path(path).read_text())
    return sorted(
        (Board.create(**board) for board in data["board"]),
        key=attrgetter('start_on'),
        reverse=True,
    )

@cache
def load_current_board(path: Path | str = BOARDS_CONFIG_PATH) -> Board:
    """Load the board that is currently in power"""
    return next(board for board in load_boards(path) if board.has_started)
