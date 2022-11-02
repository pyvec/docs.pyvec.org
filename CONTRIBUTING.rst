.. _contributing:

Jak přispívat do této dokumentace
=================================

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/pyvec/docs.pyvec.org>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt vyžaduje Python 3.7.

#. Stáhněte projekt: ``git clone https://github.com/pyvec/docs.pyvec.org.git``
#. Vytvořte si a aktivujte virtuální prostředí
#. Nainstalujte do prostředí závislosti: ``python -m pip install -r requirements.txt``

Běžná práce
-----------

#. Ve virtuálním prostředí spusťte projekt: ``sphinx-autobuild . _build``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek
#. Projekt zastavíte v terminálu pomocí :kbd:`Ctrl+C`

Emoji
^^^^^

Při psaní můžete používat Emoji jako třeba |:cz:| nebo |:snake:|, ale nepište je přímo pomocí Unicode, ale za pomocí značek jako ``|:cz:|`` nebo ``|:snake:|``. Unicode znaky by se zobrazovaly na každém operačním systému jinak, ale tyto značky budou díky rozšíření `emojicodes <https://github.com/sphinx-contrib/emojicodes>`__ přeloženy na obrázky a ty se zobrazí vždy všem stejně. Mrkněte na `seznam podporovaných Emoji <https://sphinxemojicodes.readthedocs.io/>`__. Obrázky jsou z `Twemoji <https://twemoji.twitter.com/>`_.

Slack
^^^^^

Při psaní lze psát ``:slack:`#pyladies``` nebo i jenom ``:slack:`pyladies```, což vytvoří odkaz na kanál :slack:`#pyladies` na Pyvec Slacku. Funguje to díky vlastnímu rozšíření Sphinxu, které lze najít v souboru ``_extensions/slack.py``.

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

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.7. Z toho důvodu ji vyžaduje i tento projekt. Nastavení je v souboru ``.readthedocs.yml`` (`dokumentace <https://docs.readthedocs.io/en/latest/config-file/v2.html>`_).

Continuous Integration
----------------------

Na repozitáři jsou zapojeny `GitHub Actions <https://github.com/pyvec/docs.pyvec.org/actions>`_. Kontrolka:

.. image:: https://github.com/pyvec/docs.pyvec.org/actions/workflows/build.yml/badge.svg
    :target: https://github.com/pyvec/docs.pyvec.org/actions
    :alt: Continuous Integration Status

CI je pouze informativní a nezabrání tomu, aby se hlavní větev dostala do ReadTheDocs.

.. _generate_grants:

Skript na generování zápisů hlasování o grantech
------------------------------------------------

V adresáři ``_scripts`` je skript ``generate_grants.py``, který:

* se pomocí `GitHub Actions <https://github.com/pyvec/docs.pyvec.org/actions>`_ jednou denně spustí
* vygeneruje soubor ``operations/grants.rst`` z dat na `pyvec/money <https://github.com/pyvec/money>`_ a ze šablony ``operations/grants.rst``
* commitne a pushne jej přes Git do repozitáře.

Hlasování o grantech probíhá :ref:`pomocí reakcí <jak-hlasovani>` na GitHub Issues a tento skript hlasování archivuje sem do dokumentace pro účely jednoduššího vyhledávání, zálohy, kdyby se s `pyvec/money <https://github.com/pyvec/money>`_ něco stalo, a pro nějakou historickou evidenci. Kanonickým zdrojem pravdy ale zůstává hlasování přímo na GitHub Issues, toto je jen automatizovaný přepis.
