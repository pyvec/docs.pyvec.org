"""
Sphinx extension which adds a new role :gh-repo:, which allows you to easily
make links to GitHub repositories. Example::

    There's Twitter account :gh-repo:`pyvec/docs.pyvec.org`.
"""

from docutils import nodes


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def gh_repo(name, rawtext, text, lineno, inliner, options=None, content=None):
    url = f"https://github.com/{text}"
    node = nodes.reference(rawtext, f"{text}", refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role("gh-repo", gh_repo)
    return {"version": "1.0", "parallel_read_safe": True}
