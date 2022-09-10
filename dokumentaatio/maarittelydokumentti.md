# Määrittelydokumentti

## Sovelluksen tarkoitus
Sovelluksella on tarkoitus vertailla ja visualisoida IDA* sekä Dijkstran 
reitinhakua annetussa syötteessä.

## Toteutus
Käyttäjä määrittelee alueelle koon, ja sen jälkeen piirtää
siihen seiniä sekä valitsee lähtö- ja loppupaikan. Sen jälkeen voidaan
valita joko visualisointi tai vertailu. Visualisoinnissa ohjelma piirtää valitun
algoritmin toimintaa annetulle syötteelle. Vertaillessa algoritmeja suoritus 
tapahtuu taustalla ilman visualisointia.

## Algoritmit
Tarkoituksena on löytää lyhin reitti kahden paikan välillä annetussa syötteessä.
Tarkoituksena on erityisesti tarkastella, millaisessa tilanteessa IDA* on 
parempi kuin Dijkstra ja toisinpäin.  

Mikäli aikaa jää, niin vertailuun lisätään myös A*.

#### IDA*
Tavoitteena aikavaativuudeksi O(nm) ja tilavaativuudeksi on käytännössä nykyinen polku.

#### Dijkstra
Tavoitteena aikavaativuudeksi O(n + m log n) ja tilavaativuudeksi O(n). Dijkstralle tulen
tekemään toteuttamaan prioriteettijonon itse ohjeiden mukaisesti.

## Muuta
* Ohjelmointikieli: Python
  * Muita osattuja kieliä: Java, Kotlin, JavaScript
* Dokumentointi: suomeksi
* Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

## Lähteet
* [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [https://en.wikipedia.org/wiki/Dijkstra's_algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)