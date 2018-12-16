.. _contributing:

Jak přispívat do příruček?
==========================

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/pyvec/guide>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt využívá Python 3.6 a `pipenv <https://docs.pipenv.org/>`_.

.. tabs::

    .. group-tab:: Standardní instalace

        #. Nainstalujte si Python 3.6
        #. `Nainstalujte si Pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`__
        #. ``git clone ...``
        #. ``pipenv install --dev``

    .. group-tab:: macOS

        Na macOS je problém sehnat Python 3.6, `Homebrew <https://brew.sh/>`_ vám totiž pomocí ``brew install python3`` nainstaluje novější verzi. Použijte `pyenv <https://github.com/pyenv/pyenv>`_:

        1. ``brew install pyenv``
        2. ``pyenv install 3.6.6``

        Potom pokračujte jako ve standardní instalaci, akorát je třeba napovědět, který Python chcete použít:

        3. `Nainstalujte si Pipenv <https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv>`__
        4. ``git clone ...``
        5. ``pipenv install --dev --python="$(pyenv root)/versions/3.6.6/bin/python"``

Běžná práce
-----------

#. ``pipenv run serve``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek

ReadTheDocs
-----------

Na GitHubu jsou pouze zdrojové texty. Po každé změně ve větvi ``master`` na GitHubu se automaticky vygenerují webové stránky na službě `ReadTheDocs <https://pyvec-guide.readthedocs.io/>`_. Následující kontrolka ukazuje, zda se poslední změny povedlo dostat až do webových stránek (zelená), nebo se to nepovedlo kvůli nějaké chybě (červená):

.. image:: https://readthedocs.org/projects/pyvec-guide/badge/?version=latest
    :target: https://readthedocs.org/projects/pyvec-guide/builds/
    :alt: Documentation Status

Pokud se něco nepovedlo, podrobnosti lze zjistit na `této stránce  <https://readthedocs.org/projects/pyvec-guide/builds/>`_, která je ovšem přístupná jen administrátorům.

Závislosti
----------

Projekt využívá `pipenv <https://docs.pipenv.org/>`_, ale ReadTheDocs jej zatím nepodporují (`rtfd/readthedocs.org#3181 <https://github.com/rtfd/readthedocs.org/issues/3181>`_). Proto je nutné vždy při změně závislostí zavolat ``pipenv run requirements`` a tím vytvořit i soubor ``requirements.txt``, kterému ReadTheDocs rozumí.

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.6. Z toho důvodu ji vyžaduje i tento projekt. Nastavení je v souboru ``readthedocs.yml`` (`dokumentace <https://docs.readthedocs.io/en/latest/yaml-config.html>`_).

Continuous Integration
----------------------

Na repozitáři je zapojený `Travis CI <https://travis-ci.org/>`_. Kontrolka:

.. image:: https://travis-ci.org/pyvec/guide.svg?branch=master
    :target: https://travis-ci.org/pyvec/guide
    :alt: Continuous Integration Status

Travis CI je pouze informativní a nezabrání tomu, aby se ``master`` větev dostala do ReadTheDocs.
