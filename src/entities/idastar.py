import sys
import time

from util.enums import GridType, ResultType
from util.coordinates_helper import y_out_of_bounds, x_out_of_bounds, manhattan


class IDAStar:

    def __init__(self, grid, start, end, draw=None):
        self.grid = grid
        self.start = start
        self.end = end
        self.draw = draw
        self.final_path = None

        # Init
        self.start_time = -1
        self.bound = manhattan(self.start, self.end)
        self.path = [self.start]
        self.t = -1

    def step(self):
        """Ottaa yhden askeleen algoritmille
        """
        self.t = self.step_next(self.path, 0)
        if self.t == ResultType.FOUND:
            return

        if self.t == sys.maxsize:
            self.final_path = ResultType.NOT_FOUND
            return

        self.bound = self.t

    def step_next(self, path, g):
        """Ottaa seuraavan askeleen, ja palauttaa arvon
        kunnes löytää reitin tai raja tulee vastaan

        :param path: nykyinen polku
        :param g: hinta, millä nykyinen solmu löydetään
        :return: ResultType tai uusi raja
        """
        if self.start_time != -1:
            # If over 10 seconds, return not found
            if time.time_ns() - self.start_time > 10000000000:
                self.final_path = ResultType.NOT_FOUND
                return ResultType.NOT_FOUND
        else:
            self.start_time = time.time_ns()

        # Take the last node from path and calculate (f)
        # the estimated cost to reach end ( start ... node(s) ... end )
        node = path[-1]
        f = g + manhattan(node, self.end)

        # If the estimation goes over bound,
        # the bound needs to be increased for next step
        if f > self.bound:
            return f

        if node == self.end:
            # Found end pos, set final path and return
            self.final_path = self.path, self.bound
            return ResultType.FOUND

        # Used to keep track of minimum cost to reach "last" node
        minimum = sys.maxsize

        # Move 1 in all directions
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (node[0] + move[0], node[1] + move[1])

            if x_out_of_bounds(self.grid, new_pos[0]) \
                    or y_out_of_bounds(self.grid, new_pos[1]):
                continue

            if self.grid[new_pos[1]][new_pos[0]] == GridType.WALL:
                continue

            # If new pos is not yet in the path
            if new_pos not in path:

                if self.draw:
                    self.draw(new_pos[0], new_pos[1], GridType.VISITED)

                path.append(new_pos)

                # Take the next step after this one with
                # 1 higher cost to reach
                t = self.step_next(path, g + 1)

                if t == ResultType.FOUND:
                    return ResultType.FOUND

                if t < minimum:
                    minimum = t

                path.pop()

        return minimum
