# Määrittelydokumentti

## Sovelluksen tarkoitus
Sovelluksella on tarkoitus vertailla ja visualisoida IDA* sekä Dijkstran 
reitinhakua annetussa syötteessä.

## Toteutus
Käyttäjä määrittelee alueelle koon, ja sen jälkeen piirtää
siihen seiniä sekä valitsee lähtö- ja loppupaikan. Sen jälkeen voidaan
valita joko visualisointi tai vertailu. Visualisoinnisa ohjelma piirtää valitun
algoritmin toimintaa annetulle syötteelle. Vertaillessa algoritmeja suoritus 
tapahtuu taustalla ilman visualisointia.

## Algoritmit
Tarkoituksena on löytää lyhin reitti kahden paikan välillä annetussa syötteessä.
Nyt valinnaksi osui IDA* ja Dijkstra.

#### IDA*


#### Dijkstra


* Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)
* Mitä algoritmeja ja tietorakenteita toteutat työssäsi?
* Mitä ongelmaa ratkaiset ja miksi valitsit kyseiset algoritmit/tietorakenteet?

-> Mikäli aihe on IDA* vs Dijkstra, tulee Dijkstran algoritmin prioriteettijono toteuttaa itse tehokkaasti keolla, mutta IDA*:n pinona voi käyttää valmista tietorakennetta.

## Muuta
* Ohjelmointikieli: Python
  * Muita osattuja kieliä: Java / Kotlin (+ Gradlen käyttö), JavaScript
* Dokumentointi: suomeksi
* Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

## Lähteet
* https://en.wikipedia.org/wiki/Iterative_deepening_A*
* https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm