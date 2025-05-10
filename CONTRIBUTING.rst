.. _contributing:

Jak přispívat do této dokumentace
=================================

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/pyvec/docs.pyvec.org>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Bude k tomu potřeba `uv <https://docs.astral.sh/uv/>`_:

#. Stáhněte projekt: ``git clone https://github.com/pyvec/docs.pyvec.org.git``
#. Nainstalujte: ``uv sync --group=dev``

Běžná práce
-----------

#. Ve virtuálním prostředí spusťte projekt: ``uv run pyvec-docs build``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek
#. Projekt zastavíte v terminálu pomocí :kbd:`Ctrl+C`

Markdown
^^^^^^^^

Původně byla dokumentace psaná v reStructuredText. Nyní ale podporuje i Markdown. Asi zatím nebudeme přepisovat původní stránky, ale pokud chce někdo napsat něco nového, a vyhovoval by mu spíš Markdown, nechť klidně použije Markdown.

Kdyby s tím byl nějaký problém, tady je `návod na kombo Sphinx + MyST <https://docs.readthedocs.io/en/stable/guides/migrate-rest-myst.html>`__.

Emoji
^^^^^

Při psaní můžete používat Emoji jako třeba |:cz:| nebo |:snake:|, ale nepište je přímo pomocí Unicode, ale za pomocí značek jako ``|:cz:|`` nebo ``|:snake:|``. Unicode znaky by se zobrazovaly na každém operačním systému jinak, ale tyto značky budou díky rozšíření `emojicodes <https://github.com/sphinx-contrib/emojicodes>`__ přeloženy na obrázky a ty se zobrazí vždy všem stejně. Mrkněte na `seznam podporovaných Emoji <https://sphinxemojicodes.readthedocs.io/>`__. Obrázky jsou z `Twemoji <https://github.com/twitter/twemoji>`_.

Slack
^^^^^

Při psaní lze psát ``:slack:`#pyladies`` nebo i jenom ``:slack:`pyladies``, což vytvoří odkaz na kanál :slack:`#pyladies` na Pyvec Slacku. Funguje to díky vlastnímu rozšíření Sphinxu, které lze najít v souboru ``_extensions/slack.py``.

Všechny odkazy na kanál ``:slack:`#pyvec-board``, ať už je to ``:slack:`#pyvec-board`` nebo ``:slack:`#pyvec-board-2019-2021`` jsou automaticky předělány na odkaz na aktuální tajný kanál výboru. K určení správných roků se využívá `soubor boards.toml <https://github.com/pyvec/docs.pyvec.org/blob/master/src/pyvec_docs/boards.toml>`_.

.. _docs-pyvec-rtd:

ReadTheDocs
-----------

Na GitHubu jsou pouze zdrojové texty. Po každé změně ve větvi ``master`` na GitHubu se automaticky vygenerují webové stránky na službě `ReadTheDocs <https://pyvec-guide.readthedocs.io/>`_. Následující kontrolka ukazuje, zda se poslední změny povedlo dostat až do webových stránek (zelená), nebo se to nepovedlo kvůli nějaké chybě (červená):

.. image:: https://readthedocs.org/projects/pyvec-guide/badge/?version=latest
    :target: https://readthedocs.org/projects/pyvec-guide/builds/
    :alt: Documentation Status

Pokud se něco nepovedlo, podrobnosti lze zjistit na `této stránce  <https://readthedocs.org/projects/pyvec-guide/builds/>`_, která je ovšem přístupná jen administrátorům.

Pyvec Guide
-----------

Tento projekt se původně jmenoval ``pyvec-guide`` a proto se tak jmenuje i projekt na ReadTheDocs. Projekt nemá smysl přejmenovávat, když máme nyní doménu ``docs.pyvec.org``, akorát bychom rozbili staré odkazy. JavaScript ``_static/redirect.js`` zajišťuje, že staré odkazy se přesměrují.

Verze Pythonu
-------------

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.12. Z toho důvodu ji vyžaduje i tento projekt. Nastavení je v souboru ``.readthedocs.yml`` (`dokumentace <https://docs.readthedocs.io/en/latest/config-file/v2.html>`_).

Continuous Integration
----------------------

Na repozitáři jsou zapojeny `GitHub Actions <https://github.com/pyvec/docs.pyvec.org/actions>`_. Kontrolka:

.. image:: https://github.com/pyvec/docs.pyvec.org/actions/workflows/test.yml/badge.svg
    :target: https://github.com/pyvec/docs.pyvec.org/actions
    :alt: Continuous Integration Status (test)

CI je pouze informativní a nezabrání tomu, aby se hlavní větev dostala do ReadTheDocs.

Kontrola rozbitých odkazů
-------------------------

Na repozitáři je zapojená `GitHub Action <https://github.com/lycheeverse/lychee-action>`_, která jednou denně kontroluje, zda všechny odkazy fungují. Kontrolka:

.. image:: https://github.com/pyvec/docs.pyvec.org/actions/workflows/check_links.yml/badge.svg
    :target: https://github.com/pyvec/docs.pyvec.org/actions
    :alt: Continuous Integration Status (check links)

Dokonce by to mělo automaticky zakládat i issue, pokud to najde nějaký problém. V případě, že je potřeba ignorovat nějakou doménu nebo konkrétní odkaz, je možné to udělat v souboru ``lychee.toml``.

.. _generate_files:

Generování stránek a souborů
----------------------------

Některé stránky a soubory se generují automaticky pomocí skriptů. Tyto skripty se spouští pomocí `GitHub Actions <https://github.com/pyvec/docs.pyvec.org/actions>`_, konkrétně workflow ``generate.yml``. Tyto skripty se spouští jednou denně a generují soubory, které se pak posílají jako pull requesty do repozitáře, pokud vytvoří nějaké změny.

- Generuje se ``docs/operations/boards.rst`` ze `souboru boards.toml <https://github.com/pyvec/docs.pyvec.org/blob/master/src/pyvec_docs/boards.toml>`_ a ze šablony ``operations/boards.rst``.
- Generuje se ``docs/operations/grants.rst`` z dat na `pyvec/money <https://github.com/pyvec/money>`_ a ze šablony ``operations/grants.rst``.
- Generuje se ``docs/_static/twemoji.min.js``, abychom Twemoji měli lokálně a nemuseli se spoléhat na CDN.

Kód pro generování je v ``src/pyvec_docs/cli.py``. Skripty jde pouštět např. ``uv run pyvec-docs gen-boards``.
