# Based on Python's heapq implementation

def heappush(heap, value):
    """Lisää arvon prioriteettijonoon sekä järjestää sen uudelleen

    :param heap: lista, jota käytetään prioriteettijonona
    :param value: lisättävä arvo
    """
    heap.append(value)
    down(heap, 0, len(heap) - 1)


def heappop(heap):
    """Poistaa ja palauttaa pienimmän arvon prioriteettijonosta sekä järjestää sen uudelleen

    :param heap: lista, jota käytetään prioriteettijonona
    :return: pienin arvo jonosta
    """
    value = heap.pop()
    if not heap:
        # Last value in list -> return it
        return value

    # heap[0] is min value
    # -> replace it with largest value (pop returns largest value)
    return_value = heap[0]
    heap[0] = value
    up(heap, 0)
    return return_value


def down(heap, start_position, position):
    """Prioriteettijono on järjestyksessä kaikille >= start_position,
    paitsi position indeksin osalta. Position indeksin kohdassa jono
    on mahdollisesti epäjärjestyksessä, esimerkiksi juuri on kutsuttu
    heappush, joka vain lisää loppuun uuden arvon.

    :param heap: lista, jota käytetään prioriteettijonona
    :param start_position: indeksi mihin asti tehdä tarkistus
    :param position: mahdollisesti väärässä paikassa olevan arvon indeksi
    """

    new_value = heap[position]

    # Loop till start position while moving parents
    # down until place for new value is found
    while position > start_position:

        # Like Python does, bitwise operation to divide by 2
        parent_position = (position - 1) >> 1
        parent = heap[parent_position]

        if new_value < parent:
            # Move the parent down since new value is less
            heap[position] = parent
            position = parent_position
            continue

        # Correct position found
        break

    # Last insert the new value to its correct place
    heap[position] = new_value


def up(heap, position):
    """Oletuksena on, että positionin lapset ovat jo prioriteettijonossa ns. oikein,
    mutta position indeksi ei mahdollisesti ole. Metodi etsii oikean paikan uudelle
    arvolle, jonka jälkeen kutsuu down metodia järjestääkseen arvot alusta siihen asti

    :param heap: lista, jota käytetään prioriteettijonona
    :param position: indeksi mistä aloitetaan
    """

    end_position = len(heap)
    start_position = position
    new_value = heap[position]

    child_position = 2 * position + 1
    while child_position < end_position:
        right_position = child_position + 1
        if right_position < end_position \
                and not heap[child_position] < heap[right_position]:
            # Child position is first the left leaf, here
            # the left is NOT smaller than right, so we want
            # to continue with the right leaf
            child_position = right_position

        heap[position] = heap[child_position]
        position = child_position
        child_position = 2 * position + 1

    # Insert the value to found spot
    heap[position] = new_value
    down(heap, start_position, position)
