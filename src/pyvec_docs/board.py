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
    members: list[BoardMember]

    model_config = {"extra": "forbid", "frozen": True}

    @property
    def years(self) -> tuple[int, int]:
        start_year = self.start_on.year
        return (start_year, start_year + BOARDS_MANDATE_LENGTH)


@cache
def load_boards(path: Path | str = BOARDS_CONFIG_PATH) -> list[Board]:
    data = tomllib.loads(Path(path).read_text())
    return sorted(
        (Board(**board) for board in data["board"]),
        key=attrgetter("start_on"),
        reverse=True,
    )
