from docutils import nodes


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def slack(name, rawtext, text, lineno, inliner,
          options=None, content=None):
    url = f"https://pyvec.slack.com/app_redirect?channel={text.lstrip('#')}"
    node = nodes.reference(rawtext, text, refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role('slack', slack)
    return {'version': '1.0', 'parallel_read_safe': True}
