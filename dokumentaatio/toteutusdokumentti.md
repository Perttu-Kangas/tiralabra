# Toteutusdokumentti

Hieman vaikeahko tätä vielä alkaa kirjoittelemaan. `UILogic` vastaa ohjelman logiikasta.
Sen kautta pystytään tällä hetkellä hoitamaan piirtäminen sekä aloittamaan joko Dijkstra tai IDA*.

## Ohjelman yleisrakenne
```
index.py
  entities
    dijkstra.py: vastaa Dijkstra toiminnasta
    idastar.py: vastaa IDA* toiminnasta
  services
    algorithm_ticker.py: vastaa algoritmien statistiikasta sekä juoksemisesta
    ui_logic.py: vastaa kaikesta ui logiikasta
  tests
    kaikki testit
  ui
    main_view.py: ohjelman päänäkymä
    ui.py: apuluokka helpottamaan mahdollisesti uusien näkymien tekemistä
  util
    coordinates_helper.py: pieniä apumetodeja helpottamaan koordinaattien kanssa
    enums.py: enumeita määrittelemään gridin tyyppejä sekä algoritmien tuloksia
    heap.py: minimikeko toteutus
```

## Saavutetut aika- ja tilavaativuudet

todo (viikko 6)

## Suorityskyky- ja O-analyysivertailu

todo, dijkstra parempi, jos esteitä on paljon, muuten IDA* (viikko 6)

## Työn mahdolliset puutteet ja parannusehdotukset

todo (viikko 6)

## Lähteet
* [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [https://en.wikipedia.org/wiki/Dijkstra's_algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* [https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)