.. _contributing:

Jak přispívat do této dokumentace
=================================

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/pyvec/docs.pyvec.org>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt vyžaduje Python 3.7 a `pipenv <https://pipenv.kennethreitz.org/>`_.

.. tabs::

    .. group-tab:: Standardní instalace

        #. Nainstalujte Python 3.7
        #. `Nainstalujte pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`_
        #. Stáhněte projekt: ``git clone https://github.com/pyvec/docs.pyvec.org.git``
        #. Vejděte do projektu: ``cd docs.pyvec.org``
        #. Nainstalujte projekt: ``pipenv install --dev``

    .. group-tab:: macOS

        `Homebrew <https://brew.sh/>`_ vám standardně nainstaluje nejnovější Python, což nemusí nutně být Python 3.7. Následující návod ukazuje, jak z toho ven.

        #. Koukněte se, jakou verzi Pythonu máte: ``python3 --version``
        #. Jestliže máte verzi 3.7, pokračujte jako ve standardní instalaci. Pokud máte jinou verzi, pokračujte následujícími body -- použijte `pyenv <https://github.com/pyenv/pyenv>`_ k doinstalování verze 3.7.
        #. Nainstalujte pyenv: ``brew install pyenv``
        #. Bohužel si pyenv neumí domyslet celé číslo verze, pokud mu dáme jen 3.7. Zjistěte tedy `v tomto seznamu na python.org <https://www.python.org/downloads/mac-osx/>`_, jaká je poslední vydaná verze Pythonu 3.7 (např. 3.7.5).
        #. Použijte zjištěnou verzi a nainstalujte Python 3.7: ``pyenv install 3.7.5``

        Potom pokračujete jako ve standardní instalaci, akorát je třeba napovědět, který Python chcete použít:

        #. `Nainstalujte pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`_
        #. Stáhněte projekt: ``git clone https://github.com/pyvec/docs.pyvec.org.git``
        #. Vejděte do projektu: ``cd docs.pyvec.org``
        #. Nainstalujte: ``pipenv install --dev --python="$(pyenv root)/versions/3.7.5/bin/python"``

Běžná práce
-----------

#. Spusťte projekt: ``pipenv run serve``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek
#. Projekt zastavíte v terminálu pomocí :kbd:`Ctrl+C`

Emoji
-----

Při psaní můžete používat Emoji jako třeba |:cz:| nebo |:snake:|, ale nepište je přímo pomocí Unicode, ale za pomocí značek jako ``|:cz:|`` nebo ``|:snake:|``. Unicode znaky by se zobrazovaly na každém operačním systému jinak, ale tyto značky budou díky rozšíření `emojicodes <https://github.com/sphinx-contrib/emojicodes>`__ přeloženy na obrázky a ty se zobrazí vždy všem stejně. Mrkněte na `seznam podporovaných Emoji <https://sphinxemojicodes.readthedocs.io/>`__. Obrázky jsou z `Twemoji <https://twemoji.twitter.com/>`_.

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

Závislosti
----------

Projekt využívá `pipenv <https://pipenv.kennethreitz.org/>`_, ale ReadTheDocs jej zatím nepodporují (`rtfd/readthedocs.org#3181 <https://github.com/readthedocs/readthedocs.org/issues/3181>`_). Proto je nutné vždy při změně závislostí zavolat ``pipenv lock --requirements > requirements.txt`` a tím vytvořit i soubor ``requirements.txt``, kterému ReadTheDocs rozumí.

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.7. Z toho důvodu ji vyžaduje i tento projekt. Nastavení je v souboru ``.readthedocs.yml`` (`dokumentace <https://docs.readthedocs.io/en/latest/config-file/v2.html>`_).

Continuous Integration
----------------------

Na repozitáři je zapojeno `CircleCI <https://circleci.com/>`_. Kontrolka:

.. image:: https://circleci.com/gh/pyvec/docs.pyvec.org/tree/master.svg?style=svg
    :target: https://circleci.com/gh/pyvec/docs.pyvec.org/tree/master
    :alt: Continuous Integration Status

CircleCI je pouze informativní a nezabrání tomu, aby se ``master`` větev dostala do ReadTheDocs.
