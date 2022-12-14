def x_out_of_bounds(grid, x):
    """Tarkastaa onko x koordinaatti rajojen ulkopuolella

    :param grid: [y][x] grid
    :param x: x koordinaatti
    :return: True, jos rajojen ulkopuolella
    """
    return x < 0 or x >= len(grid[0])


def y_out_of_bounds(grid, y):
    """Tarkastaa onko y koordinaatti rajojen ulkopuolella

    :param grid: [y][x] grid
    :param y: y koordinaatti
    :return: True, jos rajojen ulkopuolella
    """
    return y < 0 or y >= len(grid)


def normalize(grid_size, num):
    """Normalisoi annetun koordinaatin vastaamaan lähintä arvoa gridin koon perusteella

    :param grid_size: gridin yksittäisen objektin koko
    :param num: normalisoitava koordinaatti
    :return:
    """
    return num // grid_size


def manhattan(start, end):
    """https://en.wiktionary.org/wiki/Manhattan_distance

    :param start: alkupiste (x, y)
    :param end: loppupiste (x, y)
    :return: Manhattan distance alun ja lopun välillä
    """

    return abs(end[0] - start[0]) + abs(end[1] - start[1])
