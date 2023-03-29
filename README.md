# Hjärnmask

Ett litet program som spottar ur sig slumpvist genererade kommentarer, konstruerad utifrån de riktiga kommentarer som finns på Sverigedemokraternas propagandakanal "Riks" på youtube.

## Användning

### Installation

Programmet behöver ingen installation, allt som egentligen krävs är två av filerna från projektet: "`brainworms.py`" och "`markov_2gram_riks.tar.bz2`". Om du läser denna fil på `github.com` så kan du hitta de två filerna i listan av filer ovan denna text. Du kan också hitta en `zip`-fil som innehåller alla filer under rubriken "Releases" till höger. Packa upp eller lägg filerna på valfri plats på datorn.

#### Krav

För att köra programmet krävs Python, som du kan installera [härifrån](https://www.python.org/downloads/).

### Att köra programmet

Efter du har installerat Python och laddat ner de filer som behövs kan du köra programmet genom att starta kommandoradstolken, e.g. `cmd` i Windows (jag antar att Linuxanvändare och övrigt vet hur man gör), och navigera dit du la projektet. Sen kan projektet startas med:
```
python brainworms.py
```
Vilket ger dig obegränsat med nya kommentarer, en åt gången. Vill du istället ha flera på en gång kan du testa till exempel:
```
python brainworms.py 10
```
Vilket annat argument som helst ger ett hjälpmeddelande:
```
python brainworms.py h
Usage: brainworms.py [n]

 Args:
        n: Number of comments to print. Zero gives unlimited comments, interactively. Default: 0.
```

Notera att programmet tar en liten stund att starta och stänga ner, ta det bara lugnt.

### Efter du kört programmet

Programmet behöver inte filen "`markov_2gram_riks.tar.bz2`" efter den körts första gången, endast den nya filen "`markov_2gram_riks.json`". Du kan då, om du vill, ta bort "`markov_2gram_riks.tar.bz2`". Hela programmet tar ca. 180M med "`.tar.bz2`"-filen, och ca. 150M utan den.

## Exempel

```
$ python brainworms.py 5

----------------------------------------

Jamshof forsätt att trycka ner andra. Se alltid lösningen ❤Tack ❤

----------------------------------------

Vetenskap och forskning är. Det behövs fler nationalistiska partier som stödjer denna extremist och kränker föräldrarna till de stora förbrukarna och drivs av avund! Profilfråga driver nu eller stannar vid deras dörr matta

----------------------------------------

Samhällstjänst!! Tack underbara Katerina Du är alltid samhällsskadligt slöseri. Tack!

----------------------------------------

Patienterna har tagit över Sverige och talar emot att bränna Sverigeflaggan?

----------------------------------------

Recept på semla från SVT, denna snubbe? han är muslim- nej nu jävlar!! RASISTJÄVEL!!

----------------------------------------

```

## Varning

Detta program kan nästan garantera total [hjärnmask](https://www.youtube.com/watch?v=THUFzmmKMPs&t=97s). Det kan också hända att den genererar texter som innehåller extrem antisemitism, islamofobi, andra typer av rasism, transfobi, homofobi, andra typer av hotfullt språk emot LGBTQIA+ personer, hot om våld, glorifiering av krig, antidemokratiska påståenden, fascistiska hundvisslor, nazistiska konspirationsteorier, klimatförändringsförnekande, annat förnekande av vetenskap, och mycket mycket mer. Vi som utvecklare av detta projekt tar såklart avstånd från allt detta. Men det är kanske inte så förvånande att detta händer med tanke på var det underliggande materialet kommer ifrån.

## Delning och vidareutveckling

Skaparen av, och alla som bidrar till, detta projekt avsäger sig all upphovsrätt till projektet och menar att projektet är allmän egendom, fri att delas och användas på det sätt man vill.

Den data som används finns i filen `markov_2gram_riks.tar.bz2`, eller i uppackad form `markov_2gram_riks.json`. Se huvudprogrammet, `brainworms.py`, för ett exempel på hur man kan använda den. Du är fri att använda denna data precis hur du vill.

## Annat

Vill du ta del av mer kul? Kolla [Vörttuben](https://www.reddit.com/r/Vorttuben/comments/xpdqpm/lista_p%C3%A5_v%C3%B6rttubare_och_annan_v%C3%B6rtrelaterad/).
