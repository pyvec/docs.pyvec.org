from docutils import nodes


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def twitter(name, rawtext, text, lineno, inliner,
            options=None, content=None):
    text = text.lstrip('@')
    url = f"https://twitter.com/{text}"
    node = nodes.reference(rawtext, f'@{text}', refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role('twitter', twitter)
    return {'version': '1.0', 'parallel_read_safe': True}
