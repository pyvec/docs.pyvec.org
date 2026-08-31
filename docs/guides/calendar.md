# Jak funguje kalendář akcí

Na webu Python.cz se nachází [kalendář](https://python.cz/akce/) nadcházejících srazů, konferencí
a dalších akcí české pythonní komunity. Tyto akce se oznamují též na [Slacku](https://pyvec.slack.com/) v kanálech {slack}`#calendar` (při každé změně) a {slack}`#announcements` (týdenní souhrn).

Celý kalendář se sestavuje každý den dynamicky z různých zdrojů. Lze si jej též [stáhnout](https://python.cz/events.ics) ve formátu [iCal](https://cs.wikipedia.org/wiki/ICalendar).

## Jak přispívat

### Pravidelné akce

Pravidelné akce lze přidat přes tzv. iCal export. Ten může generovat přímo vaše webová stránka (jako v případě [pyvo.cz](https://pyvo.cz/)), nebo jej lze vytáhnout z nějaké služby (Google Calendar, meetup.com).

URL exportu pak na náš web přidejte do souboru [static/data/events_feeds.yml](https://github.com/pyvec/python.cz/edit/master/pythoncz/static/data/events_feeds.yml) repozitáře [pyvec/python.cz](https://github.com/pyvec/python.cz) pomocí pull requestu. Po začlenění se akce objeví rovnou a následně se budou načítat samy každý den.

### Jednorázové akce

Jednorázové akce lze přidat přes Google kalendář [Czech Python Events](https://calendar.google.com/calendar/embed?src=kfdeelic1a13jsp7jvai861vfs%40group.calendar.google.com&ctz=Europe%2FPrague). Do kalendáře má přístup mnoho z organizátorů existujících Python akcí. Poproste je, ať vaši akci přidají, nebo napište na [info@pyvec.org](mailto:info@pyvec.org). První URL z popisu události se zobrazí jako odkaz.

## Jak to funguje

Sestavení kalendáře se spouští automaticky jednou denně jako [akce GitHubu](https://github.com/pyvec/python.cz/actions). Spouští se též při každém začlenění změn.

Akce z nově přidaného kalendáře se tedy stáhnou okamžitě, v případě těch přidaných do stávajících kalendářů to může trvat do druhého dne. Chcete-li to uspíšit, řekněte někomu z organizátorů, nebo napište na [info@pyvec.org](mailto:info@pyvec.org), ať sestavení (akci GitHubu) spustí ručně.
