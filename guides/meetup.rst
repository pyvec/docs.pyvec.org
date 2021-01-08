.. _srazy:

Jak pořádat Python sraz (Pyvo)
==============================

.. Protože Sphinx umožňuje odkazování napříč dokumenty, hodí se mít názvy odkazů unikátní. Z toho důvodu všechny odkazy v této příručce začínají 'srazy-'.

Tato příručka si klade za cíl shromáždit veškeré zkušenosti, jež jsme za roky pořádání srazů nasbírali, aby si je mohl kdokoliv přečíst a na jejich základě založit vlastní sraz. Zároveň by bylo hezké, kdyby se stala kodexem toho, jak se správné Pyvo má dělat, kdyby sledovala nejnovější trendy a změny a kdyby díky společnému úsilí zůstala v souladu s tím, co se na srazech reálně praktikuje.

.. image:: ../_static/images/ukulele.svg
    :width: 30%
    :align: center


Python v ČR
-----------


.. _srazy-kultura:

Kultura
^^^^^^^

Python komunitě v ČR se povedlo sjednotit se. To ale neznamená, že existuje nějaká silná organizační struktura a všichni musí poslouchat někoho, kdo jim rozkazuje. Jednota spočívá v tom, že se respektujeme, spolupracujeme, táhneme za jeden provaz, že jsme našli společnou řeč, věci vymýšlíme společně, vzájemně se podporujeme a pomáháme si. Přitom zůstáváme samostatní v tom, co děláme.

Pokud se chceš zapojit, jsi vřele vítán. Máš právo výše popsanou kulturu vyžadovat od druhých, ale také pamatuj, že aby mohla přetrvat, máš nepsanou povinnost ji i dodržovat.


.. _srazy-slovnicek:

Slovníček
^^^^^^^^^

- **Pyvo** je název, který se v ČR používá pro lokální sraz uživatelů programovacího jazyka Python.
- **Pyvec** je název neziskovky, která v ČR podporuje aktivity kolem programovacího jazyka Python (viz :ref:`srazy-pyvec`). Pyvec srazy neorganizuje, je jim akorát při ruce, kdyby něco potřebovaly. Srazy může pořádat kdo chce.


.. _srazy-web:

Web
^^^

Hlavním rozcestníkem komunity je sice `python.cz <https://python.cz/>`__, ale srazy mají vyhrazený svůj vlastní web, `pyvo.cz <https://pyvo.cz/>`__. Jako i všechno ostatní co se tvoří pro Python komunitu u nás, i tento web `je Open Source <https://github.com/pyvec/pyvo.cz>`__ a může do něj přispět kdokoliv.


Mám založit sraz?
-----------------

Pokud ve tvém městě sraz ještě neexistuje, rozhodně můžeš založit místní Python sraz a pojmenovat ho Pyvo. Rádi ti pomůžeme se vším, co budeš potřebovat, zařadíme tě do kalendářů a budeme váš sraz propagovat. Rádi také přijedeme. Jestliže ve tvém městě už sraz je, tak jeho organizátoři rozhodně uvítají, pokud se k nim přidá někdo další, kdo jim pomůže - ať už jen s nějakou drobností, názorem, nebo i naplno s provozem události.

Při zakládání nového srazu je rozumné myslet na několik věcí:

- Nikdo ti neříká, jaký koncept tvůj sraz bude mít. Většinou jde o přednášky a pivo, ale můžeš si to udělat jak chceš. Pokud vymyslíš něco originálního, tím lépe! Nemusíte mít přednášky a nemusíte mít pivo. Můžete se sejít jen tak a povídat si, poznat se. I to má velkou hodnotu.
- Na druhou stranu, sraz je sraz... Neformální setkání místních. Nedělej z toho konferenci! Nezaplácni večer šesti přednáškama, nezvi 100 účastníků, nevyžaduj od lidí absolutní pozornost nebo dokonalé chování. Ideálně by se na srazu neměl bát nikdo vystoupit a říct něco ze svých zkušeností. Měli by na něj mít dveře otevřené začátečníci. Když někdo zvorá přednášku - nevadí, o nic nejde! Sraz je pro komunitu podhoubí, je to místo, kde se světoví přednášející a vševědoucí profesionálové teprve rodí.
- Nemusíte se scházet každý měsíc. Je úplně v pořádku pořádat Pyvo jednou za půl roku, za dva měsíce, klidně i nepravidelně, jednou za čas, když uzraje chuť. Na menších městech nemusí být taková návštěvnost, abyste naplnili místnost každý měsíc, zvlášť specifickým tématem, jakým je Python.
- Naše republika je malá a stále efektivnější doprava ji každým dnem zmenšuje. Jestliže je 20 minut autobusem od tvého města jiný sraz na podobné téma, tak by bylo dobré nejspíš zvážit, zda není vhodnější s ním spojit síly.
- Existují ve tvém okolí nějaké firmy, které při práci používají Python? Univerzita? Víš o nějakých jednotlivcích? Klidně se vás může scházet pět, ale znáš to - víc hlav víc ví. Zvaž šance na úspěch a podle toho zkus vymyslet formát, četnost, apod.
- Za zkoušku nic nedáš! Když zarezervuješ místnost pro deset lidí a vytroubíš do světa, že u vás bude Python sraz, tak i kdyby nikdo nepřišel, pořád se nestala žádná újma.
- Na to, abys založil sraz, nepotřebuješ znát Python. Zvládání srazu je úplně jiná práce. Kontakty, zkušenosti apod. nejsou podmínkou, ale odměnou.


Založení srazu
--------------


.. _srazy-koncept:

Koncept
^^^^^^^

Jak bylo už naznačeno, Pyvo v Brně, Praze nebo Ostravě má většinou formát následující:

#. 19:00 začátek a představování,
#. zhruba 19:30 začátek přednášek,
#. několik přednášek na předem dohodnuté a propagované téma,
#. volitelně *lightning talky*, tzn. striktně pětiminutové příspěvky bez následující diskuse na libovolné téma od kohokoliv v místnosti,
#. volná zábava (čistý networking, který trvá většinou do té doby, než se vytratí poslední návštěvník, viz :ref:`srazy-volna-zabava`).

Není nutné se tohoto formátu držet. Na srazech se dá dělat spousta věcí a od nich se pak odvíjí i výběr místa, termínu, četnosti srazu, a tak dále. Nápady na aktivity:

- Code reviews,
- kino - koukání na vybraná videa z `pyvideo.org <https://pyvideo.org/>`__,
- volné povídání,
- ukázky vlastních projektů,
- sprint - společná práce na Open Source projektech,
- přednášky nebo konzultace pro úplné začátečníky,
- grilování (odlehčené letní vydání),
- hardware bazar - účastníci donesou kousky starého hardwaru a vyměnují si je mezi sebou,
- minikonference - vydání s více přednáškami a s několika známými přednášejícími,
- výjezd - zajedete se podívat na sraz v jiném městě nebo státě.

Výše uvedené lze různě kombinovat podle situace a sraz například ozvláštňovat speciálními vydáními. Je na tobě, co vymyslíš!


.. _srazy-datum:

Vhodné datum konání
^^^^^^^^^^^^^^^^^^^

Podívej se do kalendáře existujících Pyv a pokus se nastavit datum tak, aby nekolidovalo alespoň s těmi vzdálenostně nejbližšími srazy. Jen tak umožníš lidem z okolí, aby si na tvé Pyvo udělali výlet. Pokud je sraz pravidelný, je dobré jej dělat ve všední den večer - po práci a po škole. Tradičně všechna Pyva v republice začínají v 19:00, ale nikdo tě nenutí to dodržovat. Pátky a víkendy můžou fungovat pro ojedinělé akce, nicméně většinou v tyto dny lidi odjedou užívat si volno, takže by jich zřejmě moc nepřišlo.

Pravidelná Pyva by si měla stanovit nějaký interval a držet se ho. Např. každý poslední čtvrtek v měsíci nebo každá druhá středa v měsíci. Pokud by na daný den vycházel státní svátek, Vánoce apod., je dobré udělat výjimku a důkladně ji propagovat. Nemá moc smysl konat Pyvo ve dnech volna, ze stejného důvodu jako jsou nevhodné víkendy. Pokud máš pocit, že nepřijde mnoho lidí třeba v létě, udělej klidně prázdninovou pauzu, nebo jen nějaký odlehčený speciál.


.. _srazy-misto:

Vhodné místo konání
^^^^^^^^^^^^^^^^^^^

Vhodné místo závisí na tom, jakou bude sraz mít náplň a jak často se koná. Jestliže vás bude deset a neplánujete mít přednášky, asi není moc co řešit - sejít se můžete prakticky kdekoliv.

Pro standardní Pyvo s přednáškami je dobré, pokud máte k dispozici:

- Nekuřácký salonek se zásuvkou a zavíracími dveřmi,
- možnost požádat obsluhu o vypnutí hudby v salonku,
- projektor a plátno,
- Wi-Fi.

Většina doposud existujících srazů se odehrává v nějakém pohostinství, ať už je to hospůdka, soukromý klub nebo kavárna. Je dobré myslet na přístupnost podniku. Pyvo by sice bez piva nebylo tak úplně Pyvem, ale na druhou stranu, čím méně to bude připomínat nálevnu, tím větší je pravděpodobnost, že na váš sraz přijde ostýchavější abstinent, křehčí dívka nebo středoškolák (představte si, jak doma mamce obhajuje, že jde do zakouřeného pivního pajzlu, protože se tam schází kamarádi co umí programovat). Ideální je buď soukromý klub nebo něco mezi restaurací a kavárnou. Ani moc nepřemýšlej nad tím, že to uděláš někde, kde se nedá najíst. Většina lidí, kteří na sraz dorazí, se tam bude chtít navečeřet (nebo nejen chtít, ale i muset, protože jim to tak vyšlo).

Rovněž rozmysli, zda se dá do místa konání pohodlně dostat z jiných částí města nebo z autobusového či vlakového nádraží. Ta jsou důležitá pro přespolní - a to nejsou jen návštěvníci z jiných srazů, ale i vzdálenější místní. Třeba v Brně jsou někteří pravidelní účastníci srazu z Kuřimi, což je město 15 km vzdálené.

Zvaž bezpečnost účastníků. Za temných zimních večerů není příjmné chodit kolem parku nebo lesa. Pokud není snadné se na místo konání dostat (např. není zvenčí označeno), zorganizujte před každým srazem pravidelné setkání na dobře rozlišitelném místě a nové účastníky do místa konání doveďte.

Projektor lze v nouzi půjčit pro účel srazu z větší firmy, ale musíš se s ním pak nosit. Když najdete místo s nějakou velkou televizí a není vás moc, je to celkem rozumná náhrada. Plátno lze nahradit kusem stěny nebo bílým ubrusem (vyzkoušeno). Také lze koupit rozkládací plátno, které se pak na místo přinese, roztáhne a za pár minut je vše připraveno.

.. note::
    Coworkingová centra, univerzity nebo firemní zasedačky jsou určitě také možnost, ale napříč komunitou se zatím docela shodujeme na tom, že je to ukrutná nuda a nespojuje to lidi. Sraz by měl být odpočinkem po práci a měl by ulehčit navázání a utužování vztahů mezi lidmi. Sejít se ve firemní zasedačce a při zářivkovém světle si tam dát pizzu s kolou... to prostě nemá tu správnou atmosféru. I když potom uděláš "after-party" v hospůdce, většina lidí se ti rozuteče po cestě a nebude to o ničem. Nerozděluj části večera, nesnaž se z toho udělat konferenci, neupřednostňuj přednášky před lidmi a networkingem. Jako nějaký speciál dobrý, ale na pravidelný sraz asi spíš ne. Viděli jsme to u jiných, zkoušeli jsme to dokonce sami, a není to prostě ono.

.. note::
    Pokud si můžeš vybírat, zvol místo, které má bezbariérový přístup. Je škoda vyloučit z Python komunity lidi na vozíku jen proto, že hospoda, kde se scházíte, je ve sklepě a vedou do ní pouze schody. Je jasné, že už tak je to s místy opravdu těžké a toto je další omezení, ale zkus na něj myslet. Méně schodů může v některých případech potěšit třeba i lidi, kteří přijedou na kole.


.. _srazy-fransiza:

Franšíza
^^^^^^^^

Zvaž, jestli pro tvé město není Python příliš úzké zaměření srazu. Např. ve Valašském Meziříčí jsou `Tkalci <http://tkalci.cz/>`__, sraz obecnější, o webu a dalších technologiích. V Českých Budějovicích je `Čtvrtkon <https://www.ctvrtkon.cz/>`__, který pravidelně střídá témata z různých oblastí.

V Pyvci přemýšlíme nad tím, jestli bychom nemohli zkusit zavést možnost franšízování značky Pyvo. Že by například Tkalci mohli mít jedno vydání čistě s přednáškami ze světa Pythonu a díky tomu by toto konkrétní setkání mohli prohlásit za Pyvo. Tím by se dostalo do našich kalendářů na `pyvo.cz <https://pyvo.cz>`__ a pomohli bychom jej propagovat na sociálních sítích a i jinde. Také bychom třeba vyslali nějakou delegaci výletníků (přednášejících?).

Nemáme to nijak skvěle promyšlené. Pokud by měl o tohle tvůj sraz zájem, dej nám vědět (viz :ref:`srazy-pyvec`).


.. _srazy-organizatori:

Počet organizátorů
^^^^^^^^^^^^^^^^^^

Pokud se povedlo sraz trochu rozjet, je dobré najít si lidi, kteří by mohli s organizací pomoci. Alespoň jeden parťák dokáže vyřešit situace jako je nemoc, dovolená nebo nedostatek volného osobního času na organizaci.

Dalo by se říci, že čím více lidí je v organizačním týmu, tím lépe. Při větším počtu je ale potřeba dávat si pozor na syndrom *je nás dost, udělají to ostatní*. Osvědčilo se zavést funkci hlavního organizátora, který je zodpovědný za konkrétní sraz v kalendáři a i pokud mu nikdo nepomůže, on zodpovídá za organizaci daného srazu a proaktivně se snaží vše zařídit. Také by to měl být on, kdo má poslední slovo, pokud se organizátoři zrovna snaží domluvit na něčem ohledně daného srazu - může rozhodnout jaké bude téma nebo kdo bude přednášet. Tato funkce potom spravedlivě rotuje tak, aby se všichni vystřídali. Je-li sraz každý měsíc a organizátoři jsou třeba čtyři, vychází potom na každého zorganizovat tři srazy za rok, a to už se dá zvládnout i s časově náročnou prací, rodinou, nebo jinými zájmy. Pokud někdo zjistí, že termín, který slíbil, nemůže zorganizovat, tak si jej vymění s kolegou za nějaký jeho termín, aby zůstalo rovnoměrné rozložení.

V Praze zase praktikují dělbu práce - jeden pravidelně posílá e-mail, druhý vždy shání přednášející, a tak dále.


Příprava akce
-------------


.. _srazy-rezervace:

Rezervace místa
^^^^^^^^^^^^^^^

Když se rezervuje celý salonek, berou si podniky někdy zálohu (s tím by případně dokázal finančně pomoci :ref:`srazy-pyvec`), většinou se lze ale domluvit jen tak, s příslibem větší útraty pijících a večeřících návštěvníků srazu (v Brně lze bez zálohy rezervovat i pro 70 osob).

Pokud jste našli opravdu dobré místo a máte pravidelný sraz, domluvte se s majiteli na dlouhodobé rezervaci, ať máte jistotu, že vám podnik nikdo nevyblokuje. Rezervujete-li sraz po srazu, vyplácí se udělat rezervaci přímo na místě už před odchodem z předešlého srazu. Jinak se totiž musí do podniku zavolat během následujícího měsíce a programátoři jsou bohužel někdy, ač třeba jinak velcí organizátoři, duše plaché. To znamená, že aby nemuseli volat cizím lidem, odsouvají rezervaci ze dne na den celý měsíc, pak se ji snaží udělat dva dny před akcí. Tak mohou snadno dospět k tomu, že místo už zabral někdo jiný.

Hodí se prozkoumat různá místa ve vašem městě a mít nějaké do zálohy, kdyby to ve vašem oblíbeném z nějakých důvodů nevyšlo.


.. _srazy-pyvocz:

Informace na pyvo.cz
^^^^^^^^^^^^^^^^^^^^

Před každým setkáním v předstihu přidejte informace na `pyvo.cz <https://pyvo.cz>`__.
Každý sraz je zaznamenán v `.yaml` souboru v `repozitáři na GitHubu <https://github.com/pyvec/pyvo-data>`__.

Na stránce pro konkrétní město je odkaz *přidat informace o dalším srazu*,
který otevře stránku s předvyplněnými informacemi pro další sraz.
Doplň/odkomentuj co je potřeba a pošli jako Pull Request.

Jak na složitějí úpravy (např. založení nového Pyva nebo nového místa konání)?
Často lze vše potřebné odkoukat z okolních souborů. Vždycky však můžete
`založit issue <https://github.com/pyvec/pyvo.cz/issues/>`__ s otázkou nebo,
jste-li už na našem :ref:`Slacku <slack>`, volat o pomoc v kanálu :slack:`#pyvo`.


.. _srazy-propagace:

Propagace
^^^^^^^^^

Existuje Twitter účet :twitter:`napyvo`, kam lze psát cokoliv v souvislosti s vaším srazem. :ref:`Zažádejte si o přístup <twitter>` a nebojte se tam psát. Nad toto ještě existuje robot `pyvo-twitter <https://github.com/pyvec/pyvo-twitter>`_, který píše na :twitter:`napyvo` automatické zprávy upozorňující na srazy. Upozorňuje ovšem jen na ty srazy, které jsou včas :ref:`potvrzené na pyvo.cz <srazy-pyvocz>`. Jestliže zaznamenáte nějaký problém s robotem, pište do :slack:`#automatizace`.

.. warning::
    Tato sekce ještě není zcela připravena.

..
    Lanyrd, Facebook Event + Pyonieri, Srazy.info, univerzity, firmy, Twitter... zpravicka na root.cz, zpravicka na   zdrojak, email pozvanka na django-cs / py konference, meetup.com, https://wiki.python.org/moin/PythonEventsCalendar

    Firmy!!!

    Hang some flyers at your local college; hold some meetings on a campus and get listed as a campus organization.


.. _srazy-sponzori:

Sponzoři
^^^^^^^^

.. warning::
    Tato sekce ještě není připravena.


.. _srazy-tema:

Výběr tématu
^^^^^^^^^^^^

.. warning::
    Tato sekce ještě není připravena.


.. _srazy-prednasejici:

Přednášející
^^^^^^^^^^^^

.. warning::
    Tato sekce ještě není připravena.

..
    I've found that keeping the presentations short, and maybe having two or three speakers, is a good alternative to having one speaker (unless a good speaker volunteers!). It takes some of the load off the speaker and gets more people involved.

..
    Zahraniční speakeři versus zkušení speakeři versus nováčci
    Líheň
    doporučení, jak vybrat přednášející, lightning talky
    přednášení hloupostí na lightning talku podnítí ostatní

..
    https://wiki.python.org/moin/PythonSpeakers


Průběh akce
-----------


.. _srazy-priprava:

Přicházím na místo konání
^^^^^^^^^^^^^^^^^^^^^^^^^

**Příchod**
    Pravidlo číslo jedna: Přijď na místo konání včas! Nejlépe 15 nebo 30 minut předem, aby bylo dost času vyzvednout rezervaci a vše připravit.

**Co přinést**
    Pokud se chcete jen setkat a popovídat si, nepotřebujete zřejmě žádné speciální vybavení. Pokud ale budete mít přednášky, je dobré mít při ruce:

    - Prodlužovačku (záleží i na místě konání),
    - něco jako stopky na měření délky přednášek,
    - nejrůznější redukce pro Mac (záleží i na projektoru).

**Domluva s obsluhou**
    Pokud máte salonek se zavíracími dveřmi, je možné obsluze říct, aby chodila jen pokud jsou otevřené (o přestávkách mezi přednáškami). S tím jak si návštěvníci objednávají, tak je ale takové pravidlo docela těžké dodržet. Nejlepší je asi moc to neřešit a klidně nechat přednášku přerušit obsluhou - přece jenom jsme na Pyvu a ne na velevážném kongresu státníků.

    Pokud v salonku hraje hudba, je potřeba ji nechat na přednášky vypnout. I když je velice potichu, hodně to ruší. Stejně tak může být problematické některé osvětlení.

**Placení**
    Co se placení týče, nejlepší je, pokud obsluha každému návštěvníku dává lístek zvlášť a na něj zapisuje, co si objednával. Pokud to nejde, musíš odcházet z místa konání více méně poslední a dořešit případné nesrovnalosti. Sem tam nějaké zapomenuté pivo nebývá problém, ale když lidé nezaplatí jídlo, částka může rychle naskakovat. V takovém případě je jedinou šancí je poprosit se smutným výrazem ve tváři poslední okolo postávající návštěvníky srazu o charitativní sbírku. Sice hloupá dvacka nebo pade, ale když se to nasbírá, mnohdy může být nakonec k dispozici i větší částka, než jakou je potřeba doplatit.


.. _srazy-program:

Řízení programu
^^^^^^^^^^^^^^^

Co bude součástí programu srazu, je čistě na tobě. Pokud je váš sraz inspirován tím, co je v sekci :ref:`srazy-koncept`, mohou se ti hodit následující rady:

**Uvítání, uvítací slajd**
    Až ti dojde trpělivost s čekáním na opozdilce a usoudíš, že nastal čas sraz zahájit, předstup před shromážděný lid, uzmi jeho pozornost a uvítej ho. Hodí se říct kde se návštěvníci nacházejí, jaké je téma srazu a jak to bude zhruba probíhat. Pokud jsou nějaké výrazné novinky v Python komunitě nebo v organizaci srazu, toto je ta pravá chvíle je vytáhnout.

**Představování účastníků**
    Pokud se vás nesešlo sto, na začátku udělejte kolečko jako z filmů o anonymních alkoholicích. Osvědčená šablona je:

    Ahoj, já jsem *jméno*, pracuju pro/pracuju jako *firma/volná noha*, ve volném čase rád *koníček*. Za poslední měsíc jsem *cokoliv*.

    Příklad:

    *Ahoj, já jsem Pepa Novák, pracuju pro Google, kde dělám na vyhledávání, a ve volném čase si rád hraju s RapsberryPi. Za poslední měsíc jsem na zahradě postavil žížalovník a naprogramoval jsem si super věc na setřízení empétrojek na disku.*

    Může to vypadat trapně, ale fakt se to hodí a lidem to dává šanci lépe poznat, kdo vlastně přišel, o čem se s ním mohou bavit, na co se ho mohou ptát, apod. Část "za poslední měsíc" je zajímavá především pokud se váš sraz opakuje každý měsíc a jádro pravidelných návštěvníků je stále stejné.

**Přednášky**
    Přednášky by účastníky neměly utahat. Ideální je mít dvě až tři maximálně a omezit je na 20 minut. Tento čas pak na místě hlídat. Lightning talky omezit na 5 minut a jejich čas hlídat naprosto striktně.

**Moderování diskusí**
    Je fajn, když přednáška vyvolá živelnou diskusi a všichni se nebojácně zapojují a předávají si nejrůzněší moudrosti, ale někdy už to přeroste jakousi mez a je potřeba to utnout s tím, že zbytek si dořeší o přestávce nebo během volné zábavy (viz :ref:`srazy-volna-zabava`).


.. _srazy-foceni:

Focení
^^^^^^

Focení je dobré občas udělat, aby člověk měl co použít při propagaci srazu, nebo aby měl něco na památku, ale odnést si z každé akce 100 fotek ve vysokém rozlišení asi úplně nutné není. Na většině fotek bude totiž pořád totéž: Lidi u stolu, lidi s pivem, lidi s jídlem, lidi jak si povídají, přednáška, jiná přednáška, ... K fotodokumentaci srazu postačí běžný foťák, nebo i moderní mobil, netřeba šermovat se zrcadlovkou nebo snad dokonce nahánět a platit profesionálního fotografa.

Při focení a následném sdílení výsledků své práce myslete na to, že ne každý se rád fotí a ne každý rád visí někde na Facebooku. Zpracování fotek je ještě podrobně popsáno v sekci :ref:`srazy-fotky`.


.. _srazy-nataceni:

Natáčení
^^^^^^^^

Pokud máte přednášky, můžete je natočit. To se nejlépe dělá kamerou na stativu, ale takové vybavení má málokdo. Z pravidelných návštěvníků českých Pyv je to především `Petr Viktorin <http://encukou.cz/>`__, který si je pořídil speciálně pro tento účel, objíždí s ním srazy a vše co vidí, to natáčí a následně zpracovává.

Pokud zrovna nemáte Petra ani vlastní kameru, ale přesto chcete zkusit přednášky natočit, můžete to zkusit klidně i chytrým telefonem nebo foťákem. Nakonec jde totiž při natáčení přednášejícího stejně především o zvuk. Je dobré přednášky *stříhat rovnou v kameře*, to znamená zapnout kameru těsně před začátkem přednášky a vypnout ji těsně po potlesku. Natáčení více přednášek do jednoho záběru zbytečně přináší víc nároků na následné zpracovávání záznamů.

Co ukazuje přednášející divákům je možné zachytit pomocí speciální krabičky `ExtremeCap 910 <https://www.avermedia.com/cz/product-detail/CV910>`__, která se zapojí mezi počítač a projektor a nahrává na SD kartu promítaný obraz včetně zvuku z mikrofonu. Jednu takovou krabičku má `Petr Viktorin <http://encukou.cz/>`__, druhou `Ondřej Caletka <https://ondrej.caletka.cz>`__. Alternativou je nahrávání obrazu přímo v jeho počítači pomocí programů jako

- `recordMyDesktop <https://en.wikipedia.org/wiki/RecordMyDesktop>`__
- `Quick Time <https://support.apple.com/guide/quicktime-player/record-your-screen-qtp97b08e666/10.5/mac/10.15>`__
- `FFmpeg <https://trac.ffmpeg.org/wiki/Capture/Desktop>`__ (`příklad použití <https://gist.github.com/oskar456/e887539e66af8cd045f1180f1969fab3>`__)

Jedinou překážkou může být neochota přednášejících instalovat si na počítač nějaký nový software. Argumentovat můžeš tím, že *FFmpeg* nejspíš už nainstalovaný stejně mají, *recordMyDesktop* je Open Source a *Quick Time* že je na Macu přímo součástí systému.

Obraz z počítače se dá při zpracování spojit s nahrávkou z místnosti – k tomu je dobré, aby jak nahrávka z kamery, tak nahrávka projektoru obsahovala zvuk. Přednášející by měli být snímáni v detailu a pokud možno bez plátna v záběru, aby z nich nebyla jen tmavá silueta.

Při natáčení videí a jejich následném sdílení myslete na to, že ne každý může chtít, aby byla jeho přednáška veřejně přístupná (viz :ref:`srazy-prednasejici`). Měli byste mít od přednášejícího svolení s nahráváním a uveřejněním nebo by mělo být alespoň jasné, že si mohou vybrat. Zpracování videí je ještě podrobně popsáno v sekci :ref:`srazy-videa`.


.. _srazy-volna-zabava:

Volná zábava
^^^^^^^^^^^^

Jako *volná zábava* je označován čistý networking, který trvá většinou do té doby, než se vytratí poslední návštěvník. Čím více lidí vám na srazu zůstane na networking, tím lépe, protože přesně tato část večera nejvíc přivádí lidi k sobě a utužuje komunitu. Svým způsobem je důležitější, než všechny přednášky dohromady. Jestliže návštěvníci odejdou brzy, zkus se zamyslet nad tím, zda nebyli příliš utaháni přednáškami nebo jestli je pro ně místo konání dostatečně atraktivní k delšímu setrvání. (Samozřejmě se nad tím nemusíš jen zamýšlet, můžeš se jich jednoduše zeptat).

V průběhu volné zábavy by bylo fajn, kdyby se k sobě účastníci pořád chovali jako slušní lidé i přes možné "opojení atmosférou". Alkohol je při networkingu dobrý sluha, ale zlý pán. Jakmile se někdo začne chovat tak, že by to jiné návštěvníky přivádělo do nekomfortních situací, měli by být organizátoři připraveni zasáhnout a tohoto člověka napomenout nebo jej požádat, aby akci opustil. Tvým cílem by mělo být dosažení příjemného prostředí, do kterého se nikdo nemusí bát vstoupit, ať už je to nesmělý středoškolák nebo mamina, která se zrovna vrátila ze začátečnického kurzu pořádaného `PyLadies <https://pyladies.cz/>`__. Arogance, povýšenost nad začátečníky, nejapné šikanizující vtípky nebo nemístné poznámky smrdící sexismem by se neměly tolerovat.


Knihovnička
^^^^^^^^^^^

Existuje tzv. `Knihovnička <https://github.com/pyvec/bookshelf/>`__, do které můžete darovat knihy a z níž si knihy můžete půjčovat. Přestože jsou srazy v různých městech, docela se nám zatím daří knihy distribuovat a poptávky po zapůjčkách uspokojovat (velký dík za to patří především knihovníkovi `Petru Viktorinovi <http://encukou.cz/>`__, jenž s knihami pravidelně objíždí většinu srazů v ČR). Máš-li sraz, tato Knihovnička je jednou z věcí, kterou tam můžeš docela snadno zavést a podpořit tak interakci lidí i přenos vědomostí.


Po akci
-------


.. _srazy-materialy-z-prednasek:

Materiály z přednášek
^^^^^^^^^^^^^^^^^^^^^

Jako archiv informací o jednotlivých srazech jsme využívali `Lanyrd <https://en.wikipedia.org/wiki/Lanyrd>`__, ale nakonec jsme si na `pyvo.cz <https://pyvo.cz/>`__ udělali vlastní systém s databází `pyvo-data <https://github.com/pyvec/pyvo-data>`__.

Pokud máš nějaké slajdy nebo jiné materiály, je dobré je na stránky vašeho srazu doplnit k popisu přednášek. Může to být skoro cokoliv od odkazu na YouTube s videem z přednášky, po odkazy na slajdy ze služeb jako `Speaker Deck <https://speakerdeck.com/>`__ či `SlideShare <https://www.slideshare.net/>`__. Pokud ti přednášející předá slajdy ve formě souboru, převeď je pokud možno na PDF a nahraj do repozitáře `talks-archive <https://github.com/pyvec/talks-archive>`__. Následně na ně odkazuj ve formátu ``https://pyvec.github.io/talks-archive/<název souboru>``


.. _srazy-fotky:

Fotky
^^^^^

Pyvec má na svém Google Drive archiv všech možných fotek z akcí české Python komunity, který zatím ale neústí v žádnou veřejnou, centralizovanou celorepublikovou galerii. Pokud máš nějaké fotky ze srazu (viz :ref:`srazy-foceni`) a chceš je archivovat, kontaktuj určitě :ref:`srazy-pyvec`. Chceš-li je sdílet, hoď je, kam je ti libo. Když se ti pár fotek opravdu povede, tweetni je a udělej *mention* na `@naPyvo <https://twitter.com/napyvo>`__ (rádi to retweetnem).

Při sdílení myslete na to, že ne každý se rád fotí a ne každý rád visí někde na Facebooku.


.. _srazy-videa:

Videa
^^^^^

Pokud se ti povedlo natočit nějaká videa (viz :ref:`srazy-nataceni`), buď dej vědět `Petrovi Viktorinovi <http://encukou.cz/>`__ a nebo se pokus o jejich zpracování sám/sama.

 1. Připrav prázdný adresář pro každou přednášku. S ti tím pomůže funkce ``videometadata`` nástroje `pyvodb <https://github.com/pyvec/pyvodb>`__:

.. code-block:: shell

 $ python3 -m venv venv
 $ source ./venv/bin/activate
 (venv)$ pip install git+https://github.com/pyvec/pyvodb
 (venv)$ git clone https://github.com/pyvec/pyvo-data
 (venv)$ pyvo --data pyvo-data videometadata praha 2018-07
 (venv)$ tree Praha-2018-07/
 Praha-2018-07/
 ├── config.yaml
 ├── 01-Python-bites
 │   └── config.yaml
 ├── 02-Back-end-ktery-pohani-LinuxDays-cz
 │   └── config.yaml
 └── 03-Black-The-Uncompromising-Code-Formatter
     └── config.yaml

..

 2. Do připravených adresářů nahraj soubory s videem – jak z kamery, tak záznamy projekce. Uprav vygenerovaný soubor ``config.yaml``, tak aby obsahoval správný název přednášky, jméno přednášejícího, datum a URL akce, stejně jako odkazy na videosoubory (pokud kamera automaticky dělí záběry do více souborů, nevadí to) a další metadata: jestli byla projekce 4:3 nebo 16:9, jestli jde o lightning talk, v jakém jazyku byla přednáška a v jakém slajdy, atd. Všechny možné volby najdeš v nápovědě níže zmíněného nástroje ``talk-video-maker``.

 3. Nainstaluj `talk-video-maker <https://github.com/encukou/talk-video-maker>`__ a jeho závislosti – `Inkscape <https://inkscape.org/cs/>`__, `FFmpeg <https://www.ffmpeg.org/>`__ a font `Signika Negative <https://fonts.google.com/specimen/Signika+Negative>`__. Tohle s největší pravděpodobností nebude fungovat jinde než na Linuxu. Na wiki projektu je stručný `návod, jak s tím začít <https://github.com/encukou/talk-video-maker/wiki/Jak-s-t%C3%ADm-za%C4%8D%C3%ADt>`__.

.. code-block:: shell

 (venv)$ git clone https://github.com/encukou/talk-video-maker
 (venv)$ pip install -e talk-video-maker
 (venv)$ python talk-video-maker/pyvo/make_vid.py --outdir . Praha-2018-07/01-Python-bites/config.yaml

..

 4. Pokud se vše podařilo, máš v aktuálním adresáři sestříhané video a k němu YAML soubor s metadaty potřebnými pro YouTube. Zkontroluj, jestli video vypadá, jak vypadat má, jestli nejsou překlepy v titulcích a jestli i na konci videa je synchronní obraz a zvuk. Pokud něco není v pořádku, pokus se najít příčinu – nejspíš to bude poškozený nebo špatně ustřižený video soubor.

 5. Pro nahrávání do `kanálu Pyvo na YouTube <https://www.youtube.com/channel/UCaT4I7hjX9iH1YFvNvuu84A>`__ potřebuješ vlastní Google účet. Následně požádáš `Petra Viktorina <http://encukou.cz/>`__, aby tě přidal jako správce. Na YouTube pak budeš moci přepínat mezi svými účty, přičemž jedním z nich bude právě Pyvo. Protože ruční nahrávání je otrava, existuje nástroj `talk-video-uploader <https://github.com/oskar456/talk-video-uploader>`__, který video nahraje za tebe. Při prvním spuštění tě požádá o udělení oprávnění ke konkrétnímu účtu, do kterého následně bude nahrávat všechna videa.

.. code-block:: shell

 (venv)$ pip install git+https://github.com/oskar456/talk-video-uploader
 (venv)$ talk-video-uploader
 Please visit this URL to authorize this application: https://accounts.google.com/o/…
 Enter the authorization code: 4/AAAdhr…isho
 (venv)$ talk-video-uploader *.yaml

..

 6. Po nahrání všech videí je potřeba doplnit odkazy na ně do databáze `pyvo-data <https://github.com/pyvec/pyvo-data>`__. Příslušný fragment YAML souboru vygeneruje přímo ``talk-video-uploader``. Videa jsou při nahrávání nastavena jako neveřejná. Až YouTube video zpracuje a zkontroluješ, že je všechno v pořádku, nastav ho jako veřejné přímo z webového rozhraní YouTube.

Při sdílení myslete na to, že ne každý může chtít, aby byla jeho přednáška veřejně přístupná (viz :ref:`srazy-prednasejici`). Měli byste mít od přednášejícího svolení s nahráváním a uveřejněním nebo by mělo být alespoň jasné, že si mohou vybrat.


Další informace
---------------

Pokud chceš nabrat nějakou další inspiraci k tomu, jak organizovat Python sraz, doporučujeme následující zdroje.

.. image:: ../_static/images/snake.svg
    :width: 30%
    :align: center


.. _srazy-globalni-zdroje:

Globální zdroje
^^^^^^^^^^^^^^^

- E-mailová diskuse `group-organizers <https://mail.python.org/mailman/listinfo/group-organizers>`__
- `Starting Your Python Users Group <https://wiki.python.org/moin/StartingYourUsersGroup>`__ na python.org


.. _srazy-zakulisi-cr:

Zákulisí existujících srazů v ČR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Na následujících stránkách se domlouvají organizátoři existujících srazů.

- `Pyvec Slack <https://pyvec.slack.com/>`__
- `Brno (Google Group) <https://groups.google.com/forum/#!forum/brno-pyvo>`__
- `Ostrava (Google Group) <https://groups.google.com/forum/#!forum/ostrava-pyvo>`__
- `Ostrava (Facebook) <https://www.facebook.com/groups/pyvoruby/>`__


.. _srazy-tipy:

Tipy
^^^^

- Anglicky se sraz řekne *meetup*. Lokální komunita kolem jazyka se označuje *user group*, takže sraz Python nadšenců v Olomouci bude něco jako *Meetup of the Olomouc Python User Group*.


Původ názvu Pyvo
^^^^^^^^^^^^^^^^

Název *Pyvo* vymyslel `Rastislav Turek <https://twitter.com/synopsi>`__ někdy v roce 2011. Založil skupinu `Pyonieri <https://www.facebook.com/groups/pyonieri/>`__ a odstartoval v Bratislavě srazy Pyvo, které byly ale prakticky od začátku spojené s `Rubyslavou <http://rubyslava.sk/>`__. Když Honza Javorek zakládal Python sraz v Brně, název se svolením převzal. Později se rozšířil i do Prahy (kde přejmenovali Django CS / Pyvec srazy na Pyvo) a do Ostravy, kde už se to jako Pyvo rovnou založilo. Mezitím se Rubyslava stala srazem pro programátory všeho druhu a Pyvo v Bratislavě jako samostatný projekt úplně zaniklo. Až později bylo nahrazeno komunitou kolem `PyCon SK <https://pycon.sk/>`__ a jejich srazy.


.. _srazy-pyvec:

Pyvec
^^^^^

Za touto příručkou stojí `Pyvec <https://pyvec.org/>`__, neziskovka podporující v ČR aktivity kolem programovacího jazyka Python. Pokud byste se srazem měli jakékoliv problémy, potřebovali nějaké finance nebo rady, rozhodně se na nás obraťte - jsme tu od toho, abychom vám byli k ruce a pomohli vám.

Příručku sepsal Honza Javorek. Podíleli se na ní nebo do ní nějak přispěli Petr Viktorin, Jirka Bartoň, Michal Valoušek, a další.
