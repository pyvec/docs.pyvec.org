from pathlib import Path

from jinja2 import Template

from pyvec_docs.board import load_boards


CONTENT_PATH = Path(__file__).parent.parent / "docs"


if __name__ == "__main__":
    tpl_path = CONTENT_PATH / "operations" / "boards.rst.jinja"
    tpl = Template(tpl_path.read_text())
    print(tpl.render(boards=load_boards()))
