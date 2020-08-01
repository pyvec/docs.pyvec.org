import os
from datetime import datetime
from pathlib import Path

import requests
from jinja2 import Template


REACTIONS_API_MEDIA_TYPE = 'application/vnd.github.squirrel-girl-preview'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


url = 'https://api.github.com/repos/pyvec/money/issues'
res = requests.get(url, headers={'Accept': REACTIONS_API_MEDIA_TYPE,
                                 'Authorization': f'token {GITHUB_TOKEN}'},
                   params={'per_page': 100, 'state': 'closed'})
res.raise_for_status()


def to_date(iso_datetime_string):
    iso_date_string, _ = iso_datetime_string.split('T')
    return datetime.strptime(iso_date_string, '%Y-%m-%d').date()


grants = []
for issue in res.json():
    url = issue['reactions']['url']
    res = requests.get(url, headers={'Accept': REACTIONS_API_MEDIA_TYPE,
                                     'Authorization': f'token {GITHUB_TOKEN}'})
    res.raise_for_status()

    labels = [label['name'] for label in issue['labels']]
    grants.append({
        'title': issue['title'],
        'url': issue['html_url'],
        'is_approved': 'approved' in labels,
        'created_at': to_date(issue['created_at']),
        'closed_at': to_date(issue['closed_at']),
        'votes': [{
            'username': reaction['user']['login'],
            'url': reaction['user']['html_url'],
            'content': reaction['content'],
        } for reaction in res.json()],
    })


tpl_path = Path(__file__).parent.parent / 'operations' / 'grants.template.rst'
tpl = Template(tpl_path.read_text())
print(tpl.render(grants=grants))
