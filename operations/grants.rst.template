Elektronická hlasování o grantech
=================================

Od roku 2020 o grantech :term:`výbor <Výbor>` hlasuje prostřednictvím repozitáře `pyvec/money <https://github.com/pyvec/money>`_. Zde je strojový přepis proběhlých hlasování.

.. Tento soubor je generován skriptem _scripts/generate_grants.py, neupravovat ručně!

{% for grant in grants %}
{{ grant.closed_at.day }}. {{ grant.closed_at.month }}. {{ grant.closed_at.year }} - elektronické hlasování výboru
--------------------------------------------

Dne {{ grant.created_at.day }}. {{ grant.created_at.month }}. {{ grant.created_at.year }} požádal uživatel `@{{ grant.user.username }} <{{ grant.user.url }}>`_ o grant `{{ grant.title }} <{{ grant.url }}>`_:

.. code-block:: text

{{ grant.description_indented }}

Výbor o tomto elektronicky hlasoval {{ grant.closed_at.day }}. {{ grant.closed_at.month }}. {{ grant.closed_at.year }}, kdy bylo hlasování uzavřeno s následujícím výsledkem:
{% for vote in grant.votes %}
* Uživatel `@{{ vote.username }} <{{ vote.url }}>`_: {% if vote.content == '+1' -%}
   ano
{%- elif vote.content == '-1' -%}
   ne
{%- elif vote.content == '' -%}
   zdržel se
{%- endif -%}
{% endfor %}

Grant {{ 'byl schválen' if grant.is_approved else 'nebyl schválen' }}.
{% endfor %}
