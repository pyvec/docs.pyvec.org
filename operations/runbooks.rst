Jak řešit situace
=================

.. contents::
   :depth: 2

.. _jak-clenstvi:

Jak se stát členem
------------------

**Pro koho je tento návod:** uchazeč(ka) o členství v Pyvci

#. Přečti si :ref:`stanovy`.
#. Přečti si :ref:`jak Pyvec pomáhá <podpora>`.
#. Napiš e-mail podle následující šablony a s předmětem **Žádost o členství ve spolku** jej pošli na info@pyvec.org:

   .. code-block:: text

      Ahoj,

      žádám o přijetí za člena spolku Pyvec. V komunitě jsem se již
      věnoval(a) následujícímu:

      * Pomáhal(a) jsem organizátorům hledat speakery pro Zlínské Pyvo...
      * Koučoval(a) jsem na jednom PyLadies kurzu...
      * ZÁSLUHA
      * ZÁSLUHA

      Rád(a) bych dále podpořil(a) komunitu tím, že se budu angažovat v Pyvci.
      Souhlasím se zněním stanov a souhlasím se zpracováním následujících
      osobních údajů pro účely členství ve spolku:

      JMÉNO (jak se představuješ lidem, ideálně i s příjmením - např. Honza Javorek)
      OBČANSKÉ JMÉNO (jméno a příjmení na oficiální dokumenty - např. Jan Javorek)
      DATUM NAROZENÍ
      POŠTOVNÍ DORUČOVACÍ ADRESA
      E-MAILOVÁ ADRESA (je-li jiná než ze které se posílá e-mail)
      Twitter: URL (nepovinné)
      GitHub: URL (nepovinné)
      LinkedIn: URL (nepovinné)

      Díky!

   .. note::
      Zásluh nemusí být moc, ani nemusí být žádného těžkého kalibru. Nejedná se o členství za zásluhy ani o poměřování, jde spíše o **představení se**, aby výbor věděl, s kým má tu čest. Komunita je celorepubliková a pro členy výboru nemusí být jednoduché mít přehled o všech aktivních lidech ve všech regionech.

#. Výbor by ti měl potvrdit přijetí přihlášky. Výbor bude následně o tvé přihlášce hlasovat. Záleží na vytíženosti členů výboru, ale nemělo by to nejspíš trvat déle než týden nebo dva.
#. Výbor odpoví a obeznámí tě s výsledkem hlasování. Měl by uveřejnit zápis do :ref:`zapisy` a přidat tě na Slacku do kanálu `#pyvec-members <https://pyvec.slack.com/messages/GL0H589SQ/>`__.
#. Jakmile je zápis z hlasování zveřejněn, můžeš jej spolu s e-maily použít jako důkaz o svém přijetí za člena a doklad svého existujícího členství.
#. Pyvec nemá zaveden členský poplatek, takže od této chvíle se stačí řídit :ref:`stanovami <stanovy>`.

Přijetí nového člena
--------------------

**Pro koho je tento návod:** výbor

#. Osoba žádající o členství napíše e-mail na info@pyvec.org. Tím vznikne doklad o jeho žádosti (ten e-mail, který je možné v případě potřeby dohledat).
#. V kanále `#pyvec-board <https://pyvec.slack.com/messages/G32A3QKAR/>`__ někdo nadnese:

   .. code-block:: text

      @board hlasujeme o přijetí XYZ za člena Pyvce, dejte :+1: pokud souhlasíte

#. Čeká se, dokud členové výboru odhlasují tak, že jsou :ref:`usnášeníschopní <usnasenischopnost-vyboru>`, tzn. musí odhlasovat minimálně předseda a další dva členové výboru.
#. Po hlasování někdo z výboru odpoví na e-mail (opět pro dohledatelnost) jak to dopadlo a pokud byla osoba přijata, zapíše ji do `tabulky <https://docs.google.com/spreadsheets/d/1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I/edit#gid=0>`__ a přidá do kanálu `#pyvec-members <https://pyvec.slack.com/messages/GL0H589SQ/>`__.
#. Hlasování musí být zdokumentováno jako :ref:`zapis-e-hlasovani`.
#. Jakmile je zápis z hlasování zveřejněn, nový člen jej může spolu s e-maily použít jako důkaz o svém přijetí za člena a doklad svého existujícího členství.

.. _zapis-e-hlasovani:

Zápis z jednorázového elektronického hlasování
----------------------------------------------

**Pro koho je tento návod:** výbor

#. Udělej dokumentační screenshot(y) hlasování v kanále `#pyvec-board <https://pyvec.slack.com/messages/G32A3QKAR/>`__ tak, aby šlo poznat, jak kdo hlasoval. Toto je důležité, protože na Slacku lze hlasování (klidně i omylem) zpětně změnit.
#. Ulož screenshot(y) do složky ``_static/voting`` v této dokumentaci (:ref:`jak? <contributing>`), soubory pojmenuj podle šablony ``YYYY-MM-DDTHH-MM-SS.png``.
#. Na začátek stránky :ref:`zapisy` přidej zápis podle následující šablony:

   .. code-block:: rst

      D. M. YYYY - elektronické hlasování výboru
      ------------------------------------------

      Dne D. M. OSOBA požádala e-mailem o přijetí za člena do spolku.
      Výbor o tomto jednorázově elektronicky hlasoval od D. M. do D. M., kdy bylo
      hlasování uzavřeno s následujícím výsledkem:

      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ano
      * ČLEN VÝBORU: ne
      * ČLEN VÝBORU: ano

      OSOBA byla D. M. přijata za člena spolku.

      .. image:: ../_static/voting/YYYY-MM-DDTHH-MM-SS.png

#. Pošli Pull Request s touto změnou. Před jeho přijetím by měl být schválen alespoň jedním dalším členem výboru (můžeš nastavit tým `@pyvec/board <https://github.com/orgs/pyvec/teams/board>`__ v *reviewers*).
