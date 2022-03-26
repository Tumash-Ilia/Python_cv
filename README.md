## První program

Vytvořte python program triangle.py a v něm implementujte funkci triangle. Tato funkce musí korektně určit, zda-li mohou tři čísla reprezentovat délky stran pravoúhlého trojúhelníka. Vstupem budou tři čísla, výstupem True nebo False (case sensitive).

[První program](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv01)

## Konvexní čtyřúhelník

Vaším úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, zda tvoří konvexní čtyřúhelník.
  - Příklad: body A(1, 1), B(3,1), C(3,2), D(1,3) tvoří konvexní čtyřúhelník, protože body tvoří konvexní obálku. Naopak body A(1,1), B(3,1), C(2,2), D(2,3) netvoří konvexní čtyřúhelník, protože bod C(2,2) leží uvnitř ohraničující obálky.
* Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník, ale nemusí tomu tak být pokaždé. Je potřeba aby funkce hlídala i extrémní situace, jako například, že body čtyřúhelník vůbec nevytváří. 

[Konvexní čtyřúhelník](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv02)

## Transformace dat

Cílem úkolu je vytvořit program, který transformuje data z jedné struktury do druhé.
  - Na vstupu jsou dány 3 sekvence (line_a, line_b, line_c). Každá z nich obsahuje několik uspořádaných dvojic uložených jako tuple (id, count).
  - Sekvence může tedy vypadat například takto: ((1, 3), (7, 5), (11, 3), (16, 2)). První prvek sekvence je tedy tuple s hodnotami  id = 1, count = 3. 
Oba prvky (id i count) jsou vždy celá čísla (int). Hodnoty count se mohou opakovat, id je ale unikátní a v každé sekvenci se vyskytuje nejvýše jednou.
* Vaším úkolem je spojit tyto tři sekvence do jednoho slovníku. Ten bude výstupem z programu.
* Položky slovníku budou seznamy hodnot count, klíče pak id. A to v následujícím tvaru: {id: [A, B, C]}, kde A, B a C jsou hodnoty pro příslušné ID v první, druhé a třetí sekvenci. Toto pořadí je potřeba zachovat. První pozice v seznamu tedy vždy patří první sekvenci, druhá pozice druhé atd.
  - Ovšem pozor - neplatí, že každé id je obsaženo ve všech sekvencích. Může být ve všech, ve dvou, nebo pouze v jedné. Pokud id v sekvenci není, ve výsledku bude pod daným klíčem v seznamu na místě pro příslušnou sekvenci 0. 
    
Pro lepší názornost se podívejme na jeden konkrétní příklad:
Zadané sekvence mají následující podobu:

line_a = ((1, 3), (3, 4), (10, 2)) \
line_b = ((1, 2), (2, 4), (5, 2)) \
line_c = ((1, 5), (3, 2), (7, 3))

Id 1 je tedy ve všech 3 sekvencích, id 2 a 5 ale jen ve druhé (line_b). Dále například id 7  je pouze ve třetí z nich a tak dále .Transformací sekvencí musí vzniknout následující slovník:

{1: [3, 2, 5], \
 2: [0, 4, 0],\
 3: [4, 0, 2],\
 5: [0, 2, 0],\
 7: [0, 0, 3],\
10: [2, 0, 0]}

Poznámka: id jsou zde pro lepší názornost seřazena, ale výsledek vaší funkce uspořádaný být nemusí. Klíče v normálním slovníku jsou neuspořádané.

Každá sekvence může obsahovat různá id. Pokud se pro určité id hodnota v některé sekvenci nevyskytuje, použije se nula (výchozí hodnota).

[Transformace dat](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv03)

## Caesarova šifra

Vaším úkolem je vytvořit dvě funkce. Nejprve funkci encrypt, která na vstupu přijme dva parametry - řetězec a offset a jako výstup vrátí nový řetězec. Obdobně funkce decrypt přijme řetězec a offset a vrátí řetězec původní. 

* Pro zjednodušení postačí, když funkce bude šifrovat pouze písmena  z ASCII tabulky. Nemusíte řešit české, ani jiné diakritické znaky. Funkce ovšem musí korektně zpracovat velká a malá písmena - tedy zachovat jejich velikost i v šifrovaném textu.
  - Pozor na to, že zadaný offset může být také větší než 26 - což je počet písmen bez diakritky. Ostatní znaky, jako například mezery nebo interpunkci, by funkce měla zachovat.
* Funkce crypt a decrypt jsou navzájem inverzní - což můžete využít při testu aplikace. K testu můžete využít také to, že nejčastější varianta offsetu - 13 je jedním z podporovaných kódování ve metodě encode u řetězce. Zkuste si 'ahoj'.encode('rot13'). V neposlední řadě existuje celá řada online kalkulaček tohoto kódování.

[Caesarova šifra](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv04)

## Algoritmizace problému

Tento úkol patří mezi obecné algoritmizační problémy řešitelné v libovolném jazyce. Nejde tedy jen o to vymyslet nějaké řešení, ale zamyslet se i nad jeho složitostí a efektivitou. Problém patří mezi složitější na přemýšlení, vhodný algoritmus vás nemusí napadnou hned. Doporučuji nejprve se nad tím zamyslet jen s papírem a tužkou. 
Problém, který máte vyřešit, je následující: představte si dveře, které jsou uzavřeny speciálním druhem zámku. Ten se otevírá vyřešením puzzle. Celkem častá mezihra v řadě počítačových her že?
* Puzzle tvoří jednotlivá slova na magnetických destičkách. Destičky musí být uspořádáné za sebou tak, aby poslední písmeno prvního slova, bylo prvním písmenem druhého atd.
* Příklad: za slovem kolo může následovat ondatra dále pak ananas atd.  Je to jako jednoduchý slovní fotbal.
* Použít se musí všechny destičky, které na daných dveřích jsou.
* Pokud lze zadanou množinu slov takto uspořádat, řeší puzzle a odemyká dveře. Pokud ne, dveře otevřít nejdou. Ve hře musíte jít hledat další destičky, zde bude stačit, když funkce vrátí False.

Vstupní data jsou pak uložena ve dvou souborech small.txt a large.txt. Oba soubory mají následující formát:
1. První řádek souboru je počet testovaných dveří (1-500).
2. Následuje počet slov pro dané dveře (2-100000) = N
3. A následně N řádků se slovy. Slova tvoří malá písmena anglické abecedy. Počet písmen 2 – 1000.
4. Pak následuje počet slov pro druhé dveře atd.

Vzorová vstupní data (soubor small.txt): \
4 \
2  
kolo  
karma  
3  
motyka \
apac \
acm \
2 \
ok \
ok \
4 
troubit \
trumpeta \
astat \
tesat 

A teď končeně váš úkol: napište program, který načte soubor large.txt a pro každé dveře vyhodnotí, zda je možné je otevřít nebo ne. Tedy vyhodnotí, zda lze danou množinu uspořádat požadovaným způsobem. Výstup z programu uložte do souboru vysledky.txt ve formátu 1 výsledek =  1 řádek. Na řádek napište vždy počet slov v množině a True nebo False, podle toho, zda řešení existuje nebo neexistuje.

Výstup pro soubor small.txt by měl tedy vypadat následovně:
2 False \
3 True \
2 False \
4 True 

[Algoritmizace problému](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv05)

## Regulární výrazy

Vaším dnešním úkolem je vytvořit program, který o zadaném textu zjistí některé údaje a vypíše je na standardní výstup. Hlavním smyslem cvičení je procvičit si práci s regulárními výrazy, takže pro plný bodový zisk je nutné je použít k řešení problému.

Program musí pracovat s obecným textem, který bude zadaný v souboru. Jméno souboru bude zadáno jako vstupní parametr funkce main, která by měla být vstupním bodem programu. Funkce main by neměla řešit problém kompletně a měli byste si vytvořit další pomocné funkce, podle principů SOLID (viz přednáška).

Můžete předpokládat, že soubor bude mít vždy kódování utf-8 a že bude psaný anglicky, tedy jen pomocí ASCII znaků, bez české (či jiné) diakritiky. 

Konkrétně musí program zjistit a vypsat:

1. Počet slov, která obsahují nejméně dvě samohlásky (aeiyou) za sebou. Například slovo bear.
2. Počet slov, která obsahují alespoň tři samohlásky - například slovo atomic.
3. Počet slov, která mají šest a více znaků - například slovo terrible.
4. Počet řádků, které obsahují nějaké slovo dvakrát. 

Každý výsledek vypište na jeden řádek, dodržte  pořadí úkolů 1-4 ve výpise. Případně můžete ve výpise doplnit také komentářem který výpis je který úkol. 

V prvních třech případech počítejte každé slovo pouze jednou, i pokud se v textu vyskytuje víckrát. Ve všech případech nerozlištujte velká a malá písmena. Tedy například Atomic a atomic můžete považovat za stejné slovo.

Lingvistická poznámka: v angličtině se y za samohlásku (vowel) obvykle nepovažuje. Pro toto cvičení se ale budeme držet toho, že samohlásky jsou AEIYOU. 

**Testovací příklad:**

Testovací soubor simple.txt najdete stejně jako šablonu pro řešení tradičně v repozitáři. Soubor simple obsahuje jedinou větu: “Obvious Functionality When looking at the app directory, it should be obvious what kinds of things the application does.”  

Výsledek pro tento jednoduchý soubor je: 

1. 6, konkrétně jde o slova Obvious, Functionality, looking, should, application, does
2. 5, konkrétně Obvious, Functionality, looking, directory, application
3. 7, konkrétně Obvious, Functionality, looking, directory, should, things, application
4. 1, konkrétně je to slovo obvious

V repozitáři najdete ještě soubor cv06_test.txt, který je delší a obsahuje více slov. Používal jsem ho pro testování úkolu v předchozích letech. Letos použiju jiný text, takže můžu prozradit správné výsledky pro tento soubor. 

1. 54
2. 68
3. 84
4. 16

Tolerance pro výsledky je +/- 2, takže když vám například třetí bod vyjde 85 budu to stále ještě počítat jako správné.

[Regulární výrazy](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv06)

## Zpracování JSON a HTML dat

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých souborech. 

První soubor obsahuje výsledky několika závodů - jména a časy závodníků. Druhý pak obsahuje databázi závodníků uloženou jako JSON. V databázi je krom jiných údajů, také id každého ze závodníků, které budete potřebovat najít podle jména a příjmení.

Cílem je vytvořit  program, který data z těchto dvou zdrojů propojí. Konkrétně nás bude zajímat závod štafet. Cílem je tedy ke každému závodníkovi ve štafetě pomocí programu najít jeho id.

Pozor na to, že data jsou reálná a tudíž nejsou ideální, takže nastane i případ, že id z výsledků najít nejde. I tuto situaci ale musí program korektně ošetřit a tato špatná data uložit pro další zpracování.  Výsledky bude tedy bude program zapisovat do více souborů.

<details><summary>Více</summary>
<p>

### Vstupní data

V repositáři předmětu v adresáři **cv07** najdete soubory result.html a competitors.json. 

Soubor **result.html**  obsahuje výsledky několika závodů, ale pro vás jsou důležité **pouze výsledky závodu štafet** (relay) - je to poslední ze závodů na stránce. Data jsou uložena poněkud nešťastně - jako text uvnitř jednoho odstavce v html. Jde ale o naprosto reálný příklad uložení dat na webu mezinárodní sportovní federace.

Nejprve tedy musíte tato data ze souboru vyparsovat a následně rozdělit konkrétní štafetu na jednotlivé závodníky. Pozor  - při rozdělení musíte zachovat také informaci o umístění štafety v závodě. Pořadí jednotilvých členů štafety totiž budete potřebovat pro výsledek. 

Soubor **competitors.json** obsahuje informace o sportovcích.  Jedná se vlastně o databázi, uloženou ve formátu JSON. Data jsou uložena jako list objektů. Každý objekt reprezentuje jednoho závodníka pomocí následujících informací - id, jméno, příjmení, státní příslušnost, rok narození, pohlaví. Například může vypadat takto:

{
"id": 10816,
"firstname": "Jiri",
"lastname": "Hradil",
"nationality": "CZE",
"birth": "1986",
"gender": "M"
}

**Doplňující informace k datům:**
*Jména souborů můžete v programu zapsat jako konstanty (není potřeba zadávat parametrem)
*Můžete předpokládat, že data budou vždy validní dle specifikace daného formátu - jak json tak html. 
*Můžete předpokládat, že jména závodníků obsahují pouze velká a malá ASCII písmena, mezeru a pomlčku

### Výstup z programu
Jak už bylo řečeno, je vaším úkolem **přiřadit jednotlivým závodníkům ve štafetě jejich id**. Je tedy rozumné vyhledávat nejprve příjmení, v případě že nestačí pak i křestní jméno. Můžete ale hledat i celý řetězec najednou. Složitější situace, jako že závodník má více jmen a není jasné co z toho je jméno a co příjmení, můžete ignorovat, respektive je v pořádku, když program takového závodníka označní za nedohledatelného.

Program musí **zapsat výsledky do třech souborů**. První z nich bude obsahovat kompletní výsledek, tedy všechny záznamy (pozitivní i negativní match), druhý stručný přehled nalezených a třetí ty závodníky, které se nepodařilo dohledat.

**První soubor** - tedy kompletní výsledek je třeba zapsat ve formátu JSON:

{
"id": 10816,
"result": 2
"time": "2:05:26"
}

**Při zpracování dat narazíte také na situaci, že závodníka v souboru competitors nenajdete.** Ať už proto že tam jeho jméno prostě není vůbec, nebo je v souboru s výsledky zkomolené. Problém dělají také dánská či španělská jména, která jsou typicky delší a často není zřejmé co je jméno a co příjmení.

V tomto případě uložte jako id hodnotu False a jméno závodníka zapište pod klíč "no_match". Závodníka zapište jak do souboru kompletních výsledků, tak do extra souboru errors.txt (viz dále) . Výsledek by tedy měl vypadat například  následovně:

{"id": "False","result": 1,"time": "2:25:18","no_match": "Elisabeth Hohenwarter"}

**Kompletní data ve výše uvedeném formátu zapište souboru output.json jako list slovníků.**  Aby soubory s řešením bylo možné porovnat, použitjte pro metodu json.dumps následující nastavení: json.dumps(results, indent=4, sort_keys=True).  Ve vzorovém souboru relay.py je metoda output_json, kterou můžete využít pro uložení. Nebo pro inspiraci jak má vypadat formátování.

**Druhý soubor compare.txt bude jednoduchý txt formát**. Na každý řádek v souboru zapište jedno nalezené id mezeru a pořadí závodníka. Id v tomto případě musí být seřazená vzestupně. Závodníky, kteří mají id = False v tomto výstupu ignorujte. 

**Třetí soubor bude opět jednoduchý txt soubor. Soubor se bude jmenovat errors.txt.** Na každý řádek zapište, jméno závodníka, kterého se nepodařilo dohledat. Tedy závodníky, které jste ve druhém souboru vynechali.

**Další požadavky:**

* Zdrojová data nesmíte nijak upravovat (nahrazovat znaky apod.) 
* Váš modul musí být v adresáři cv07 a musí se jmenovat relay.py. 
* Do repozitáře neukládejte soubory s výsledky - nechte výsledný program aby je vytvořil. Zdrojové soubory v repozitáři být mohou.
* Můžete využít pouze built-in balíčky ze standardní instalace Pythonu 3.x. Dále můžete využít parser BeautiflSoup (BS4) pokud chcete. A samozřejmě vaše vlastní balíčky.
* Výsledný kód musí při testu programem PyLint se standardním nastavením získat alespoň 8 bodů. Za každý bod dolů, máte bod dolů i vy

**Nápověda na závěr:**

* Snadno si spočítáte, že štafet bylo v závodě celkem 24 - 9 ženských a 15 mužských. To dává celkem 72 jmen či id. 
* Problematických jmen je ve výsledcích štafet celkem 10 či 9 (záleží na algoritmu jméno+příjmení)
* Soubor compare.txt bude tedy mít 62(63) řádků. První řádek - tedy nejmenší id je 182 6, poslední řádek pak 18442 1.

</p>
</details>


[Zpracování JSON a HTML dat](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv07)

## Tvorba vlastního typu

Znáte karetní hru Black Jack, nebo její  českou varitantu "Voko bere"? Dnešní úkol je vytvořit vlastní typ, reprezentující karty pro tuto hru, pomocí klíčového slova class a speciálních metod.

Vámi vytvořená třída **Card** bude reprezentovat hrací kartu pro hru Black Jack. Třídě implementujte následující metody, atributy a vlastnosti chování:

* Základní konstruktor přijímajicí hodnoty rank a suit - pomocí speciální metody __init__  
* Rank je hodnota karty od 2 do 14 (2..10, J, Q, K=13, A=14), suit je barva karty (srdce, kára, piky, trefy). Rank se zadává číslem 2-14, suit jedním znakem "s", "k", "p", "t".
* Pokud karta vytvořit nejde - například proto, že je špatně zadaná barva či hodnota, musí třída vyvolat výjimku **TypeError**. A to nejen při vytváření nové karty, ale i kdykoliv při pokusu o změnu hodnoty rank či suit. Dejte si pozor na to co jsme si na přednášce říkali o programování v konstruktoru a o validaci atributů.
* **rank** - atribut, který zpřístupní hodnotu karty jako číslo 
* **suit** - atribut, který zpřístupní barvu karty jako písmeno s, k, p, t
* **black_jack_rank(self)** - metoda, která vrátí hodnotu karty ve hře Black Jack. Eso je za 11 bodů, ostatní figury (K, Q, J) jsou za 10 bodů. Zbylé karty mají hodnotu danou číslem.
* Při volání **str(karta)**, kde karta je instance třídy, vrátí váš typ vhodnou textovou reprezentaci. Tedy hodnotu i barvu karty jako text - např. pikový král, srdcové eso, trefová dvojka atd. Pozor na to, že reprezentace musí být správně česky, tedy například srdcové dvojka je špatně. Pokud vám projde přiložený test, máte to v pořádku. K implementaci je potřeba využít jednu ze speciálních metod. 
* Na závěr implementujte operaci **porovnávání karet podle black_jack_rank** - budete muset implementovat hned několik speciálních metod. Nezapomeňte také na neostrá (<=, =>) porování a rovnost. Při tomto porování nezáleží na barvě karet (suit), pouze na hodnotě kartý v black jacku. 
V souboru **test_card.py** v repozitáři předmětu najdete několik základních testů pro váš typ. Nepokrývají ale všechny situace. Proto doporučuji si doplnit vlastní, jako první procvičení látky z 8. přednášky.

[Tvorba vlastního typu](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv08)

## Ovládání programu z příkazové řádky

Vytvořte program, který prohledá zadaný textový soubor a najde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více vzorů. Tyto řádky je pak potřeba z programu vypsat na obrazovku a přidat k ním jejich čísla v původním souboru.

Tak trochu se toto chování podobá unixovému příkazu **grep**, přesněji řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program toho bude umět v mnoha ohledech méně. Cílem úkolu určitě není vytvářet 100% kopii příkazu grep.

**Program musí jít  ovládat z příkazové řádky.** Základním parametrem zadávaným vždy, je jméno souboru. Pokud jméno souboru není zadané, program nemůže pracovat. V takovém případě musí zobrazit nápovědu. Jméno souboru se bude zadávat pomocí parametru -f eventuelně --filename. 

Druhý parametr  parametr -s --search bude volitelný. Může být následován **libovolným počtem n slov**. Samozřejmě, pokud je tam parametr -s musí tam být to slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí program opět vypsat chybu nebo nápovědu. 

**Požadované chování a ovládání programu:**

1. **python hledac.py -f mujsoubor.txt** - Zde chybí parametr s. Program v tomto případě vypíše na obrazovku celý soubor a ve výpisu očísluje jednotlivé řádky
2. **python hledac.py -f lipsum.txt -s orem** - Bylo zadáno jedno hledané slovo "orem". Program tedy musí vytisknout na obrazovku pouze ty řádky které obsahují řetězec orem. Nemusí se jednat o celé slovo - může jít o libovolný nepřerušený řetězec. Takže i třeba slovo řádek obsahující "Lorem ipsum". Stejně jako v prvním případě musí být jednotlivé řádky očíslované. Číslování řádku pochází z originálního souboru - program tak ukazuje, na kterém řádku se hledané slovo nachází. Příklad vzorového vstupu a výstupu máte v repozitáři v souboru lipsum_oren_uloha9.txt . Toto chování se blíží tomu co vypíše grep -n orem lorem.txt. 
3. **python hledac.py -f lipsum.txt -s dolor amet** - no a v tomto případě vypíše pouze ty řádky, které obsahují řetězec dolor a zároveň řetězec amet. Na pořadí zadaných slov v nezáleží. Opět máte k dispozici vzorový výstup, tentokrát se soubor jmenuje lipsum_dolor_amet_uloha9.txt. Pokud chcete zkusit příkaz grep pro kontrolu,  musíte využít dva (pro každé slovo 1) a propojovací rouru, nebo hledat regulární výraz. 
4. **python hledac.py** - bez zadaného souboru vypíše nápovědu, případně upozorní na chybu. Zkrácená nápověda z argparse je v tomto případě dostačující. Nemusíte vypisovat plnou nápovědu jako při volbě -h. 
5. **python hledac.py -f lipsum.txt -s** bez zadaného vzoru opět vypíše nápovědu, případně upozorní na chybu., jako v předchozím případě.
6. Program by měl rozlišovat velká a malá písmena. Tím se celý problém zjednodušuje, protože nemusíte transformovat vstup.

[Ovládání programu z příkazové řádky](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv09)

## Web scraper

**Cílem cvičení je vytvořit program, který dokáže najít co nejvíc adres**.

Váš vysledný program musí vyřešit následující úkoly:

1. **Přijmout základní url jako parametr z příkazové řádky.**  Stačí velmi základní řešení - tzn. není potřeba tentokrát použít argparse, program bude zavolán příkazem python scraper.py url. 
2. **Zjistit kolik dokumentů** tvoří prohledávanou množinu. Dokumenty jsou propojené navzájem pomocí odkazů (relativní, absolutní na stejný server), ale mohou obsahovat také odkazy na jiný server (absolutní url s jiným hostname). Tyto odkazy jinam musí váš program rozpoznat a  z dalšího prohledávání je vyřadit. 
3. **Množinu** prohledávaných dokumentů uložit **ve formě slovníku odkazů (index)**. Tedy vytvořit základní mapu stránek. Jméno aktuálního souboru slouží jako klíč slovníku, soubory odkazované z aktuálního url, jsou zapsané jako položky listu, uloženého pod tímto klíčem ve slovníku. Požadovaná struktura indexu je následující:
\
   {\
'soubor1.html' : ['soubor2.html', 'soubor3.html'], \
'soubor2.html' : ['soubor3.html', 'soubor88.html'],\
... 
}
4. Konečně - prohledat všechny nalezené dokumenty a **najít** v nich pokud možno **všechny e-mailové adresy**. Adresy jsou různě ukryté a obsahují také pokusy o jednoduchý anti-spam a obfuskaci. Pravidla pro hledané adresy:
   - pro účely tohoto cvičení platí, že platný **e-mail může obsahovat pouze malá písmena, číslice, tečky a znak @**. Ostatní znaky pokud se vyskytují jsou anti-spam a program by je měl odstranit.
   - Některé adresy jsou aktivní odkazy, ale ne všechny.
   - Některé obsahují základní pokusy o antispam, snadno rozpoznatelný
5. **Výsledky** musí program **zapsat do souboru** scrap_result.txt v tomto formátu:
   - nejprve nalezenou mapu stránek - tedy onen slovník
   - následně volný řádek
   - a pak už jednotlivé e-maily, každý na nový řádek.
    
Pro kontrolu ať si to nemusíte ručně počítat sami. Soubory jsou celkem 4 a adres je v nich různým způsobem ukryto celkem 7. Pro nalezení všech musíte zkombinovat několik různých způsobů hledání.

Program ale samozřejmě musí být univerzální, to znamená, že musí zvládnou situaci, kdy bude za stejných pravidel přidán další soubor a další adresy.

[Web scraper](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv10)

## Cenzor 

Cílem je vytvořit jednoduchý cenzorovací systém. Tedy program pro odfiltrování zadaných slov z textu. 

Vstupem do programu jsou dva soubory. První z nich je HTML stránka obsahující text, který je potřeba profiltrovat. Druhý soubor obsahuje seznam zakázaných slov v jednoduchém formátu 1 slovo = 1 řádek.

Program  musí být možné  ovládat argumenty z příkazové řádky.

**Ovládání programu musí zvládnou následující parametry:**

* -i, --input : soubor který má být upraven (běžný text)
* -l, --list : soubor se seznamem zakázaných slov - jedno slovo jeden řádek
* -c, --clean : přepínač vyčištění souboru od html - viz. dále
* -o, --output: výstupní soubor, pokud není volba použita, tak vypsat data na obrazovku
* -h, --help : nápověda - o čem program je a jak se ovládá

**Požadované vlastnosti:**
1. Pokud je skript spuštěn s parameterm -c (--clean) tak odstranit z textu všechny HTML značky - to znamená na výstup pouze text.
2. Nahradit všechna zakázaná slova v textu sekvencí znaků #. Délka nahrazené sekvence musí být rovná délce původního (nahrazeného) slova.
3. Pokud bude program spuštěn s parametrem -o jméno, vypsat výstup do souboru jméno. Jinak vypisovat na obrazovku.

**Slova v textu**: pro dělení slov můžete použít metodu split u řetězce, nebo u regulárního výrazu, což umožňuje dělit rovnou i přes složitější kombinace interpuknčích znamének, nejen přes jeden konkrétní řetězec (mezera, čárka apod.)

**HTML značky**: jsou formátovací sekvence HTML. Od běžného textu jsou odděleny znaky < a >.

[Cenzor](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv11)

## Hledání tajných čísel

Jistá nejmenovaná tajná agentura používá již nějakou dobu, jako kódy pro přístup do tajného skladu následujících sedum čísel: 

**56003, 56113, 56333, 56443, 56663, 56773, 56993**

Když čísla v této sedmiprvkové množině blíže prozkoumáte zjistíte, že jsou to prvočísla. 

Nejsou to ale jen tak obyčejná prvočísla - mají následující společné vlastnosti:

1. všechna mají právě 5 číslic
2. všechna mají společný základní tvar **56xx3** 
3. x - tedy 3 a 4 číslice je vždy stejná. Dosazením konkrétní číslice vznikne znovu prvočíslo. V našem případě je x postupně 0, 1, 3, 4, 6, 7 a 9
4. prvočísel s touto vlastností (dvě stejné číslice vedle sebe) je více, ale 56003 je to nejmenší z nich.

Tajné agentury ale musí čas od času tajné kódy měnit. No a váš úkol  je najít novou sadu takových tajných kódů. Čísel o něco delších a tedy coby hesel bezpečnějších. Ovšem čísel se stejnými či podobnými vlastnostmi jako mají předchozí klíče. Musí to být opět speciální prvočísla.

Konkrétní úkol zní: **najít nejmenší prvočíslo, pro které platí, že nahradíme-li jeho část stejnými číslicemi, stane se základem osmiprvkové množiny.**

Tedy podobně jako číslo 56003, které je základem množiny sedmiprvkové.  Hledané nové prvočíslo bude mít ale přece jen trochu jiné  vlastnosti:

* lze předpokládat, že **číslo bude mít minimálně šest číslic**
* **měnit se budou právě 3 číslice** (lze to matematicky dokázat, ale to nemusíte dělat :-) ). Tuto měnící číslici můžeme označit  y.
* všech **8 nových čísel musí být prvočísla** ve stejném tvaru - např. 42yyy1
* měnící se číslice **y spolu nemusí nutně sousedit** jako u původních čísel - nová čísla tedy mohou mít i tvar 876yyy ale i 4y3y2y atd.
* pro hledaná čísla platí, že měnící se číslice y je pro každé z 8 hledaných čísel jiná. Každý z prvků hledané osmiprvkové množiny je tedy jiné číslo.

**program by měl najít řešení do 1 minuty**

[Hledání tajných čísel](https://github.com/Tumash-Ilia/Python_cv/tree/main/cv12)


