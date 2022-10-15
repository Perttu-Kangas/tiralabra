# Viikkoraportti

## Viikko 6 - 5h

#### Edistyminen

Projekti ei tällä viikolla täysin edistynyt niin kuin ajattelin.
Koodin dokumentointi on kuitenkin hyvin pitkälti nyt valmis.

#### Oppiminen ja epäselvyydet

Tällä viikolla ei oikein mitään uutta tullut.

#### Tuleva viikko (loppupalautus / ennen demotilaisuutta)

Tarkoituksena olisi toteuttaa `performance_test.py` isolle ja pienelle kartalle seinien kanssa sekä ilman niitä.
Tällä pitäisi pystyä hyvin havainnollistamaan, millaisessa tilanteessa Dijkstra on parempi kuin IDA* ja toisinpäin.
Myös kaiken muunkin dokumentoinnin viimeistely.

## Viikko 5 - 8h

#### Edistyminen

Projekti edistyi suunnitelmien mukaan, eli otin algorithm tickerin käyttöön sekä lisäsin testejä.
Myös löydetyn polun piirto on nyt toteutettu.

#### Oppiminen ja epäselvyydet

Tällä viikolla ei oikein mitään uutta tullut.
Lähinnä piti miettiä kuinka toteuttaa algorithm tickerin toiminnan.

#### Tuleva viikko

Tarkoituksena olisi ottaa huomioon saatu vertaispalaute.
Myös visuaalisesti näkyville algoritmin suoritukseen kulunut aika ja askeleet.
Pääpainona on kuitenkin dokumentointi tulevalla viikolla, 
esimerkiski Dijkstra ja IDA* ei ole vielä juurikaan ollenkaan kommentoitu.

## Viikko 4 - 8h

#### Edistyminen

Projekti edistyi suunnitelmien mukaan, eli Dijkstralle prioriteettijonon toteutus, sekä IDA* toiminta.

Lisäsin enemmän testejä sekä korjasin muutaman bugin.

Suorituskykytestejä en vielä tehnyt, sillä algorithm ticker tulee käyttöön vasta ensi viikon palautukseen.

#### Oppiminen ja epäselvyydet

Tuli opittua IDA* toiminta, sekä perehdyttyä prioriteettijonon implementaation Pythonin implementaation, ja
muiden [lähteiden](https://www.geeksforgeeks.org/heap-data-structure/) avulla. Lisäksi tuli huomattua, että 
tämä EI luo uusia objekti referenssejä `[[GridType.NONE] * grid_rows] * grid_cols`, mutta tämä 
tekee `[[GridType.NONE for _ in range(gridcols)] for  in range(grid_rows)]`.

#### Tuleva viikko

Tarkoituksena on ottaa algorithm ticker käyttöön, jolla pystytään tekemään suorituskykytestejä sekä keräämään
statistiikkaa algoritmien toiminnasta. Lisäki sen jälkeen lisään testit algoritmeille, en ole tehnyt niitä vielä, 
koska algorithm tickerin käyttöönotto muokkaa hieman algoritmien luokkia myös. Tarkoituksena olisi myös lisätä
parhaimman polun piirto, kun se on löydetty myös visuaalisesti.

## Viikko 3 - 8h

#### Edistyminen

Projekti edistyi suunnitelmien mukaan, eli refaktoroin piirtotyökalun koodin, sekä toteutin Dijkstran.
Sille pitää vielä itse toteuttaa prioriteettijono.  

Lisäsin GitHub Pagesiin nähtäville [testikattavuuden](https://perttu-kangas.github.io/tiralabra/htmlcov/).   

Siirsin samalla tämän repositoryn muiden koulujuttujen ohella omaan GitHub organisaatioonsa, helpottaakseen repojen organisointia.

#### Oppiminen ja epäselvyydet

Opin ainakin Pythonia kirjoittelemaan paremmin (kouluprojekteissa vain harjoittelen Pythonin käyttöä samalla).

#### Tuleva viikko

Tarkoituksena toteuttaa Dijkstralle oma prioriteettijono, sekä IDA* toiminta

## Viikko 2 - 5h

#### Edistyminen

Projekti edistyi suunnitelmien mukaan, eli käyttöliittymä mihin voi piirtää on valmis.
Tämän koodi pitää kuitenkin vielä refaktoroida. Lisäksi tein alustavat luonnokset 
tuleville algorithm ticker, IDA* ja Dijkstra luokille.

#### Oppiminen ja epäselvyydet

Tällä viikolla alustin projektia tkinterin avulla. Uutena asiana ehkä tuli, että
siihen oli implementoitu valmiiksi Canvas, niin ei PyGamella tarvinnut lähteä säätämään nappeja yms.

#### Tuleva viikko

Tarkoituksena olisi refaktoroida nykyinen koodi, ja toteuttaa ainakin Dijkstran toiminta.

## Viikko 1 - 5h

#### Edistyminen

Aika meni pitkälti aihetta miettiessä, ja IDA* tutustumisessa.
Aiheen päättämisen jälkeen alustin projektin, ja kirjoitin määrittelydokumentin.

#### Oppiminen ja epäselvyydet

IDA* perustoimintaa tarkasteln. Sen lisäksi tuli tarkasteltua paremmin, miten Dijkstrassa prioriteettijono on toteutettu.  

Epäselvyydeksi nyt vielä jäi hieman IDA* aika- ja tilavaativuus.

#### Tuleva viikko

Tarkoituksena on toteuttaa sovellukselle visuaalinen käyttöliittymä, johon voi piirtää.
