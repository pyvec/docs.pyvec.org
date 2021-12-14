Volby do výboru
===============

Funkční období :term:`výboru <Výbor>` je dle `stanov <stanovy>`_ tři roky, členové spolku ze svých řad volí pět členů. To se děje na členské schůzi, kterou výbor k této příležitosti svolává.

Nově zvolený výbor si potom sám volí, kdo z těchto pěti bude předseda a případně kdo bude pokladník (když se nerozhodne volit pokladníka, je jím automaticky předseda).

.. note::
    Přečíst ještě `PEP 8102 <https://www.python.org/dev/peps/pep-8102/>`__ a případně se inspirovat? Dořešit.

Kdy se volí
-----------

- Předchozí volba: **8.4.2019**
- Příští volba: **?.?.2022**, předpokládá se termín březen/duben

Harmonogram pro rok 2022
------------------------

- Příprava: od 1. ledna
- Uzavírka kandidatur: do konce února

Příprava
--------

- Postupuje se podle stanov, svoláváme :ref:`členskou schůzi <clenska-schuze>`.
- Výbor na nějaké schůzi s předstihem určí přesné datum členské schůze.
- Výbor dá členům vědět, jak lze podávat nominace, jak kandidovat. Kandidovat do výboru může jakýkoliv člen Pyvce.
- Ideálně se pokusí členy motivovat k tomu, aby kandidovali, a to komunikací s členy, ukazováním toho, jak výbor pracuje, jak vypadá běžná schůze výboru (např. zveřejněním video nahrávky), apod. Výbor může také neformálně oslovovat vhodné kandidáty a přesvědčovat je, že mají kandidovat.
- Někdo z výboru vezme e-mailové adresy členů ze `seznamu členů <https://docs.google.com/spreadsheets/d/1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I/edit#gid=0>`__ a pošle jim pozvánku na členskou schůzi. Pozvánka musí obsahovat místo, čas a program jednání členské schůze. Kromě toho by měl výbor schůzi oznámit i v kanálu :slack:`#pyvec-members`. Pro inspiraci, pozvánka na členskou schůzi `EuroPython Society <https://www.europython-society.org/europython-society-general-assembly-2020/>`__.
- Ve vybrané datum se uzavřou kandidatury. Uzavření přihlášek a konečný seznam kandidátů se oznámí v kanálu :slack:`#pyvec-members`. Pro inspiraci, `kandidatury do EuroPython Society <https://www.europython-society.org/list-of-eps-board-candidates-for-20192020/>`__.

.. note::
    Kandidatury lze umístit sem do dokumentace, nebo možná lépe na blog? Dořešit.

.. note::
    EPS nelimituje kandidáty na přihlášené předem: _Please note that our bylaws do not restrict nominations to people on this list. It is even possible to self-nominate or nominate other candidates at the GA itself. However, in the interest of giving members a better chance to review the candidate list, we’d like to encourage all nominations to be made before the GA._ Dořešit.

Začátek voleb
-------------

- V datum schůze se udělá vykopávací meeting, koordinace probíhá přes :slack:`#pyvec-members`.
- Výbor členy obeznámí s technickým zázemím volby.
- Členové následně dostávají týden na to, aby asynchronně volili.

.. note::
    Jaké máme technické zázemí volby? Petr Viktorin zmiňoval, že PSF používá `Helios Voting <https://vote.heliosvoting.org/>`__.

Mechanika voleb
---------------

- Každý člen Pyvce má 5 hlasů (ve výboru je 5 lidí).
- Proběhne volba, bere se prvních pět, kteří dostanou nejvíc hlasů.
- Pokud je shoda hlasů u více kandidátů na 5. a dalším místě, volí se stejným způsobem znova mezi nimi (rekurze).
- Tímto je navolen nový výbor.

.. note::
    Tady nám nesedí to, že volba je vícekolová, ale my necháváme týden asynchronně lidi hlasovat. Dořešit.

Konec voleb
-----------

- Členská schůze přijímá rozhodnutí nadpoloviční většinou hlasů přítomných členů.
- Po týdnu voleb se uzavře hlasování a starý výbor vyhodnotí hlasy, vyhlásí výsledky přes :slack:`#pyvec-members`.
- Starý a nový výbor si naplánují meeting, kde se seznámí a dojde k cermoniálu předání moci. Starý výbor předá novému Trello board a zodpoví všechny otázky.
- Starý výbor zajistí vyhotovení zápisu ze zasedání členské schůze:

    - Vyhotoví :ref:`zápis do této dokumentace <zapisy>`_,
    - aktualizuje `soubor board.yml <https://github.com/pyvec/docs.pyvec.org/blob/master/board.yml>`_,
    - aktualizuje role členů v `seznamu členů <https://docs.google.com/spreadsheets/d/1n8hzBnwZ5ANkUCvwEy8rWsXlqeAAwu-5JBodT5OJx_I/edit#gid=0>`__, čímž by se měl aktualizovat i web Pyvce

- Starý výbor musí zápis zaslat všem členům e-mailem, opět na adresy ze seznamu členů. Toto je poslední oficiální úkol starého výboru.
- Nový výbor si musí zvolit předsedu (viz dále).
- Nový výbor dostává první závažný úkol, při kterém jej ideálně stínuje starý výbor a pomáhá mu k jeho dokončení: Kontaktovat právničky spolku, `AK Šichová <https://aksichova.cz/>`__, aby připravily papíry, kodifikovaly výsledek voleb a změnu zanesly do státního rejstříku (úkol není hotov, dokud na `justice.cz <https://www.justice.cz>`__ nejsou u Pyvce vidět nová jména).

Volba předsedy
--------------

- Nový výbor si mezi sebou musí zvolit předsedu a může zvolit :term:`pokladníka <Pokladník>`.
- Každý člen výboru má jeden hlas a funkci dostává ten, kdo má nejvíc hlasů.
