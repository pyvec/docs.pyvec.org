import os
import re
from datetime import date
from pathlib import Path
from operator import itemgetter

import requests
from jinja2 import Template
import strictyaml as yaml


REACTIONS_API_MEDIA_TYPE = 'application/vnd.github.squirrel-girl-preview'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
URL = 'https://api.github.com/repos/pyvec/money/issues'
REACTIONS_MAPPING = {'+1': 'ano', '-1': 'ne', 'eyes': 'zdržel(a) se'}

BOARD_HISTORY_SCHEMA = yaml.Seq(yaml.Map({
    'from': yaml.Datetime(),
    'members': yaml.MapPattern(yaml.Str(), yaml.Str()),
}))
BOARD_HISTORY_PATH = Path(__file__).parent.parent / 'board.yml'
BOARD_HISTORY = sorted(yaml.load(BOARD_HISTORY_PATH.read_text(),
                                 BOARD_HISTORY_SCHEMA).data,
                       key=itemgetter('from'), reverse=True)


res = requests.get(URL, headers={'Accept': REACTIONS_API_MEDIA_TYPE,
                                 'Authorization': f'token {GITHUB_TOKEN}'},
                   params={'per_page': 100, 'state': 'closed'})
res.raise_for_status()


def to_date(iso_datetime_string):
    iso_date_string, _ = iso_datetime_string.split('T')
    return date.fromisoformat(iso_date_string)


def remove_comments(html):
    return re.sub(r'<!--[^<]+-->', '', html).strip()


def get_board_member_name(username, voted_at):
    for board in BOARD_HISTORY:  # sorted from the most recent
        if voted_at > board['from'].date():
            return board['members'].get(username)
    return None


def get_votes(reactions, voted_at):
    for reaction in reactions:
        username = reaction['user']['login']
        name = get_board_member_name(username, voted_at)
        if name:  # else not reaction from a board member
            text = REACTIONS_MAPPING.get(reaction['content'])
            if text:
                yield {'name': name, 'text': text}


grants = []
for issue in res.json():
    voted_at = to_date(issue['closed_at'])

    url = issue['reactions']['url']
    res = requests.get(url, headers={'Accept': REACTIONS_API_MEDIA_TYPE,
                                     'Authorization': f'token {GITHUB_TOKEN}'})
    res.raise_for_status()
    votes = list(get_votes(res.json(), voted_at))

    labels = [label['name'] for label in issue['labels']]
    if 'approved' not in labels and 'rejected' not in labels:
        # skip unlabeled grants, e.g. https://github.com/pyvec/money/issues/1
        continue

    grants.append({
        'title': issue['title'],
        'description': remove_comments(issue['body']),
        'url': issue['html_url'],
        'user': {
            'username': issue['user']['login'],
            'url': issue['user']['html_url'],
        },
        'is_approved': 'approved' in labels,
        'filed_at': to_date(issue['created_at']),
        'voted_at': voted_at,
        'votes': votes,
    })
grants = sorted(grants, key=itemgetter('voted_at'), reverse=True)


tpl_path = Path(__file__).parent.parent / 'operations' / 'grants.rst.template'
tpl = Template(tpl_path.read_text())
print(tpl.render(grants=grants))
