# IDA* vs Dijkstra
Sovelluksella vertaillaan ja visualisoidaan IDA* ja Dijkstra -reitinhakualgoritmeja.

## Julkaisu
- [Viimeisin](https://github.com/Perttu-Kangas/tiralabra/releases/latest/)

## Dokumentaatio

- [Viikkoraportti](dokumentaatio/viikkoraportti.md)
- [Määrittelydokumentti](dokumentaatio/maarittelydokumentti.md)
- [Toteutusdokumentti](dokumentaatio/toteutusdokumentti.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md) 
- [Käyttöohje](dokumentaatio/kayttoohje.md)

## Asennus

1. Kloonaa repo
2. Asenna riippuvuudet ``poetry install``
3. Käynnistä sovellus ``poetry run invoke start``

Ohjeet Poetryn asentamiseen sen omasta dokumentaatiosta [täältä](https://python-poetry.org/docs/).

## Komentorivitoiminnot

### Ohjelman suorittaminen
Komento: ``poetry run invoke start``

### Testaus
Komento: ``poetry run invoke test``

### Testikattavuus
Komento: ``poetry run invoke coverage-report``

### Pylint
Komento: ``poetry run invoke lint``