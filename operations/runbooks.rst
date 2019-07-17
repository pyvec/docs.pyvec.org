Jak řešit situace
=================

.. contents::
   :depth: 2

Přijetí nového člena
--------------------

#. Osoba žádající o členství napíše email na info@pyvec.org. Tím vznikne doklad o jeho žádosti (ten email, který je možné v případě potřeby dohledat).
#. V kanále `#pyvec-board <https://pyvec.slack.com/messages/G32A3QKAR/>`__ někdo nadnese:

   .. code-block:: text

      @board hlasujeme o přijetí XYZ za člena Pyvce, dejte :+1: pokud souhlasíte

#. Čeká se, dokud členové výboru odhlasují tak, že jsou :ref:`usnášeníschopní <usnasenischopnost-vyboru>`, tzn. musí odhlasovat minimálně předseda a další dva členové výboru.
#. Po hlasování někdo z výboru odpoví na email (opět pro dohledatelnost) jak to dopadlo a pokud byla osoba přijata, zapíše ji do `tabulky <https://docs.google.com/spreadsheets/d/1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I/edit#gid=0>`__.
#. Hlasování musí být zdokumentováno jako :ref:`zapis-e-hlasovani`.
#. Jakmile je zápis z hlasování veřejně, nový člen jej může spolu s emaily použít jako důkaz o svém přijetí za člena a doklad svého existujícího členství.

.. _zapis-e-hlasovani:

Zápis z jednorázového elektronického hlasování
----------------------------------------------

#. Udělej dokumentační screenshot(y) hlasování v kanále `#pyvec-board <https://pyvec.slack.com/messages/G32A3QKAR/>`__ tak, aby šlo poznat, jak kdo hlasoval. Toto je důležité, protože na Slacku lze hlasování (klidně i omylem) zpětně změnit.
#. Ulož screenshot(y) do složky ``_static/voting`` v této dokumentaci (:ref:`jak? <contributing>`), soubory pojmenuj podle šablony ``YYYY-MM-DDTHH-MM-SS.png``.
#. Na začátek stránky :ref:`meeting-notes` přidej zápis podle následující šablony:

   .. code-block:: rst

      D. M. YYYY - elektronické hlasování výboru
      ------------------------------------------

      Dne D. M. OSOBA požádala emailem o přijetí za člena do spolku.
      Výbor o tomto jednorázově elektronicky hlasoval od D. M. do D. M., kdy bylo
      hlasování uzavřeno s následujícím výsledkem:

      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ne
      * ČLEN VÝBORU: ano

      OSOBA byla D. M. přijata za člena spolku.

      .. image:: ../_static/voting/YYYY-MM-DDTHH-MM-SS.png

      .. image:: ../_static/voting/YYYY-MM-DDTHH-MM-SS.png

#. Pošli Pull Request s touto změnou. Před jeho přijetím by měl být schválen alespoň jedním dalším členem výboru (můžeš nastavit tým `@pyvec/board <https://github.com/orgs/pyvec/teams/board>`__ v *reviewers*).
