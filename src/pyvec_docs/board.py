from operator import itemgetter
from pathlib import Path

import strictyaml as yaml


BOARD_HISTORY_SCHEMA = yaml.Seq(
    yaml.Map(
        {
            "from": yaml.Datetime(),
            "members": yaml.MapPattern(yaml.Str(), yaml.Str()),
        }
    )
)
BOARD_HISTORY_PATH = Path(__file__).parent / "board.yml"
BOARD_HISTORY = sorted(
    yaml.load(BOARD_HISTORY_PATH.read_text(), BOARD_HISTORY_SCHEMA).data,
    key=itemgetter("from"),
    reverse=True,
)
