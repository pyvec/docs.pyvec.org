"""
Sphinx extension which adds a new role :twitter:, which allows you to easily
make links to twitter.com profiles. Example::

    There's Twitter account :twitter:`napyvo`.
"""

from docutils import nodes


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def twitter(name, rawtext, text, lineno, inliner, options=None, content=None):
    text = text.lstrip("@")
    url = f"https://twitter.com/{text}"
    node = nodes.reference(rawtext, f"@{text}", refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role("twitter", twitter)
    return {"version": "1.0", "parallel_read_safe": True}
