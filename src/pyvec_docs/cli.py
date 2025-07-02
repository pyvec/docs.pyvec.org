import subprocess
import sys
from operator import itemgetter
from pathlib import Path

import click
import requests
from jinja2 import Template

from pyvec_docs.boards import load_boards
from pyvec_docs.grants import get_lock_date, get_votes, remove_comments, to_date


@click.group()
def main() -> None:
    pass


@main.command()
def test() -> None:
    """Run the tests"""
    try:
        subprocess.run(["pytest"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)


@main.command()
def build() -> None:
    """Build the documentation into the build directory"""
    try:
        subprocess.run(["sphinx-build", "-nWaE", "docs", "build"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)


@main.command()
def watch() -> None:
    """Serve documentation on a local webserver, rebuild on changes"""
    try:
        subprocess.run(["sphinx-autobuild", "-nWaE", "docs", "build"], check=True)
    except subprocess.CalledProcessError:
        sys.exit(1)


@main.command()
@click.option(
    "--template",
    "template_path",
    type=click.Path(exists=True, path_type=Path),
    default="docs/operations/grants.rst.jinja",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(path_type=Path),
    default="docs/operations/grants.rst",
)
@click.option(
    "--github-url", type=str, default="https://api.github.com/repos/pyvec/money/issues"
)
@click.option("--github-token", type=str, envvar="GITHUB_TOKEN")
def gen_grants(
    template_path: Path,
    output_path: Path,
    github_url: str,
    github_token: str,
) -> None:
    """Generate grants.rst (needs authorization token)"""
    github_headers = {
        "Accept": "application/vnd.github.squirrel-girl-preview",
        "Authorization": f"token {github_token}",
    }
    res = requests.get(
        github_url,
        headers=github_headers,
        params={"per_page": 100, "state": "closed"},
    )
    res.raise_for_status()
    issues = res.json()

    boards = load_boards()
    grants = []
    with click.progressbar(issues, label="Processing issues") as progress:
        for issue in progress:
            labels = [label["name"] for label in issue["labels"]]
            if "approved" not in labels and "rejected" not in labels:
                # skip unlabeled, e.g. https://github.com/pyvec/money/issues/1
                continue

            if issue["locked"]:
                res = requests.get(
                    issue["events_url"],
                    headers=github_headers,
                    params={"per_page": 100},
                )
                res.raise_for_status()

                if res.headers.get("link"):
                    raise NotImplementedError(
                        f"The number of events of issue #{issue['number']} "
                        "is paginated and the code isn't yet designed "
                        "to handle this!"
                    )
                else:
                    voted_at = get_lock_date(res.json())
            else:
                voted_at = to_date(issue["closed_at"])

            res = requests.get(issue["reactions"]["url"], headers=github_headers)
            res.raise_for_status()
            votes = list(get_votes(res.json(), voted_at, boards))

            grants.append(
                {
                    "title": issue["title"],
                    "description": remove_comments(issue["body"]),
                    "url": issue["html_url"],
                    "user": {
                        "username": issue["user"]["login"],
                        "url": issue["user"]["html_url"],
                    },
                    "is_approved": "approved" in labels,
                    "filed_at": to_date(issue["created_at"]),
                    "voted_at": voted_at,
                    "votes": votes,
                }
            )
    grants = sorted(grants, key=itemgetter("voted_at"), reverse=True)

    tpl = Template(template_path.read_text())
    output_path.write_text(tpl.render(grants=grants))


@main.command()
@click.option(
    "--template",
    "template_path",
    type=click.Path(exists=True, path_type=Path),
    default="docs/operations/boards.rst.jinja",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(path_type=Path),
    default="docs/operations/boards.rst",
)
def gen_boards(
    template_path: Path,
    output_path: Path,
) -> None:
    """Generate boards.rst"""
    boards = load_boards()
    tpl = Template(template_path.read_text())
    output_path.write_text(tpl.render(boards=boards))


@main.command()
@click.option(
    "--source-url",
    type=str,
    default="https://cdn.jsdelivr.net/npm/@twemoji/api@latest/dist/twemoji.min.js",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(path_type=Path),
    default="docs/_static/twemoji.min.js",
)
def gen_twemoji(source_url: str, output_path: Path) -> None:
    """Download the latest version of twemoji.min.js from CDN of https://github.com/jdecked/twemoji/"""
    res = requests.get(source_url)
    res.raise_for_status()
    output_path.write_bytes(res.content)
