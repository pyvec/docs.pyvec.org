import os
from datetime import datetime

import requests


REACTIONS_API_MEDIA_TYPE = 'application/vnd.github.squirrel-girl-preview'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


url = f'https://api.github.com/repos/pyvec/money/issues'
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

    grants.append({
        'title': issue['title'],
        'is_open': issue['state'] == 'open',
        'url': issue['html_url'],
        'is_approved': 'approved' in [label['name'] for label in issue['labels']],
        'created_at': to_date(issue['created_at']),
        'closed_at': to_date(issue['closed_at']),
        'votes': [{
            'username': reaction['user']['login'],
            'url': reaction['user']['html_url'],
            'content': reaction['content'],
        } for reaction in res.json()],
    })


print('.. Tento soubor je generován skriptem _scripts/generate_grants.py, neupravovat ručně!')
for grant in grants:
    title = f"{grant['closed_at'].day}. {grant['closed_at'].month}. {grant['closed_at'].year} - elektronické hlasování výboru"
    votes = '\n'.join([
        f"* {vote['username']}: {vote['content']}"
        for vote in grant['votes']
    ])
    print(f'''
{title}
{'-' * len(title)}

Dne {grant['created_at'].day}. {grant['created_at'].day}. {grant['created_at'].year} vznikl grant.
Výbor o tomto elektronicky hlasoval {grant['closed_at'].day}. {grant['closed_at'].month}. {grant['closed_at'].year}, kdy bylo hlasování uzavřeno s následujícím výsledkem:

{votes}

Grant {'byl schválen' if grant['is_approved'] else 'nebyl schválen'}.
    ''')
    print()
