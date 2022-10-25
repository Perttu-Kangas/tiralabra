# Määrittelydokumentti

## Sovelluksen tarkoitus
Sovelluksella on tarkoitus vertailla ja visualisoida IDA* sekä Dijkstran 
reitinhakua annetussa syötteessä.

## Toteutus
Käyttäjä piirtää alueelle seiniä sekä valitsee lähtö- ja loppupaikan. Sen jälkeen voidaan
valita joko visualisoida algoritmin toimintaa. Visualisoinnissa ohjelma piirtää valitun
algoritmin toimintaa annetulle syötteelle.

## Algoritmit
Tarkoituksena on löytää lyhin reitti kahden paikan välillä annetussa syötteessä.
Tarkoituksena on erityisesti tarkastella, millaisessa tilanteessa IDA* on 
parempi kuin Dijkstra ja toisinpäin.  

Mikäli aikaa jää, niin vertailuun lisätään myös A*.

#### IDA*
Tavoitteena aikavaativuudeksi `O(nm)` ja tilavaativuudeksi on käytännössä nykyinen polku.

#### Dijkstra
Tavoitteena aikavaativuudeksi `O(n + m log n)` ja tilavaativuudeksi `O(n + m)`. Dijkstralle tulen
tekemään prioriteettijonon itse ohjeiden mukaisesti.

## Muuta
* Ohjelmointikieli: Python
  * Muita osattuja kieliä: Java, Kotlin, JavaScript
* Dokumentointi: suomeksi
* Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

## Lähteet
* [https://en.wikipedia.org/wiki/Iterative_deepening_A*](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
* [https://en.wikipedia.org/wiki/Dijkstra's_algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
* [https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/](https://www.cs.helsinki.fi/u/ahslaaks/tirakirja/)