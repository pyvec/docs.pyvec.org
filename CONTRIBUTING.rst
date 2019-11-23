.. _contributing:

Jak přispívat do této dokumentace
=================================

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/pyvec/docs.pyvec.org>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt vyžaduje Python 3.6 a `pipenv <https://pipenv.kennethreitz.org/>`_.

.. tabs::

    .. group-tab:: Standardní instalace

        #. Nainstalujte si Python 3.6
        #. `Nainstalujte si Pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`__
        #. ``git clone https://github.com/pyvec/docs.pyvec.org.git``
        #. ``cd docs.pyvec.org``
        #. ``pipenv install --dev``

    .. group-tab:: macOS

        Na macOS je problém sehnat Python 3.6, `Homebrew <https://brew.sh/>`_ vám totiž pomocí ``brew install python3`` nainstaluje nejnovější verzi. Použijte `pyenv <https://github.com/pyenv/pyenv>`_:

        #. ``brew install pyenv``
        #. ``pyenv install 3.6.6``

        Potom pokračujte jako ve standardní instalaci, akorát je třeba napovědět, který Python chcete použít:

        #. `Nainstalujte si Pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`__
        #. ``git clone https://github.com/pyvec/docs.pyvec.org.git``
        #. ``cd docs.pyvec.org``
        #. ``pipenv install --dev --python="$(pyenv root)/versions/3.6.6/bin/python"``

Běžná práce
-----------

#. ``pipenv run serve``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek

Emoji
-----

Při psaní můžete používat Emoji jako třeba |:cz:| nebo |:snake:|, ale nepište je přímo pomocí Unicode, ale za pomocí značek jako ``|:cz:|`` nebo ``|:snake:|``. Unicode znaky by se zobrazovaly na každém operačním systému jinak, ale tyto značky budou díky rozšíření `emojicodes <https://github.com/sphinx-contrib/emojicodes>`__ přeloženy na obrázky a ty se zobrazí vždy všem stejně. Mrkněte na `seznam podporovaných Emoji <https://sphinxemojicodes.readthedocs.io/>`__.

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

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.6. Z toho důvodu ji vyžaduje i tento projekt. Nastavení je v souboru ``readthedocs.yml`` (`dokumentace <https://docs.readthedocs.io/en/latest/config-file/v1.html>`_).

Continuous Integration
----------------------

Na repozitáři je zapojeno `CircleCI <https://circleci.com/>`_. Kontrolka:

.. image:: https://circleci.com/gh/pyvec/docs.pyvec.org/tree/master.svg?style=svg
    :target: https://circleci.com/gh/pyvec/docs.pyvec.org/tree/master
    :alt: Continuous Integration Status

CircleCI je pouze informativní a nezabrání tomu, aby se ``master`` větev dostala do ReadTheDocs.
