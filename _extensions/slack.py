"""
Sphinx extension which adds a new role :slack:, which allows you to easily
make links to pyvec.slack.com Slack channels. Example::

    In any doubt, ask in the :slack:`#pyvo` channel.
"""

from docutils import nodes


# https://docutils.readthedocs.io/en/sphinx-docs/howto/rst-roles.html
def slack(name, rawtext, text, lineno, inliner,
          options=None, content=None):
    text = text.lstrip('#')
    url = f"https://pyvec.slack.com/app_redirect?channel={text}"
    node = nodes.reference(rawtext, f'#{text}', refuri=url, **(options or {}))
    return [node], []


def setup(app):
    app.add_role('slack', slack)
    return {'version': '1.0', 'parallel_read_safe': True}
