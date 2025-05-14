Dokumentace české Python komunity
=================================

V dokumentaci `českých Pythonistů <https://python.cz>`__ jsou návody pro organizátory komunitních akcí a také interní směrnice neziskovky `Pyvec, z.s. <https://pyvec.org/>`__, která tyto akce zaštiťuje.

Návody jsou komunitní projekt `českých Pythonistů <https://python.cz>`__.
Jejich cílem je poskytnout materiály a *know-how* pro pořadatele a částečně
i účastníky (např. kouče) různých akcí, jako jsou srazy, workshopy, kurzy.

Dokumentace je tvořena jako `otevřená <https://cs.wikipedia.org/wiki/Otev%C5%99en%C3%BD_software>`__, do jejího zdrojového kódu a textů může kdokoliv navrhovat změny. Texty a obrázky těchto materiálů jsou uvolněny pod licencí `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/deed.cs>`__.


Lokální spuštění
----------------

Dokumentaci je možné editovat přes GitHub; pro každý *pull request* se
vygeneruje náhled.
Kdo chce pracovat na svém stroji, může dokumentaci sestavit do adresáře
``build`` pomocí tohoto příkazu::

    uv run python -m sphinx build docs build
