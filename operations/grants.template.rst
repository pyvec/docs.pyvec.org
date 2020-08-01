.. Tento soubor je generován skriptem _scripts/generate_grants.py, neupravovat ručně!

{% for grant in grants %}

{{ grant.closed_at.day }}. {{ grant.closed_at.month }}. {{ grant.closed_at.year }} - elektronické hlasování výboru
---------------------------------

Dne {{ grant.created_at.day }}. {{ grant.created_at.day }}. {{ grant.created_at.year }} vznikl grant. Výbor o tomto elektronicky hlasoval {{ grant.closed_at.day }}. {{ grant.closed_at.month }}. {{ grant.closed_at.year }}, kdy bylo hlasování uzavřeno s následujícím výsledkem:
{% for vote in grant.votes %}
* {{ vote.username }}: {{ vote.content -}}
{% endfor %}

Grant {{ 'byl schválen' if grant.is_approved else 'nebyl schválen' }}.

{% endfor %}
