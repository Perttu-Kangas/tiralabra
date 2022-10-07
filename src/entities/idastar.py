import sys

from util.enums import GridType, ResultType
from util.coordinates_helper import y_out_of_bounds, x_out_of_bounds, manhattan


class IDAStar:

    def __init__(self, ui_logic, grid, start, end, draw=None):
        self.ui_logic = ui_logic
        self.grid = grid
        self.start = start
        self.end = end
        self.draw = draw
        self.final_path = None

        # Init
        self.bound = manhattan(self.start, self.end)
        self.path = [self.start]
        self.t = -1

    def step(self):
        self.t = self.step_next(self.path, 0, self.bound)
        if self.t == ResultType.FOUND:
            return

        if self.t == sys.maxsize:
            self.final_path = ResultType.NOT_FOUND
            return

        self.bound = self.t

    def step_next(self, path, g, bound):
        node = path[-1]
        f = g + manhattan(node, self.end)

        if f > bound:
            return f

        if node == self.end:
            self.final_path = self.path, self.bound
            return ResultType.FOUND

        min = sys.maxsize

        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (node[0] + move[0], node[1] + move[1])

            if x_out_of_bounds(self.grid, new_pos[0]) \
                    or y_out_of_bounds(self.grid, new_pos[1]):
                continue

            if self.grid[new_pos[1]][new_pos[0]] == GridType.WALL:
                continue

            if new_pos not in path:

                if self.draw:
                    self.draw(new_pos[0], new_pos[1], GridType.VISITED)

                path.append(new_pos)
                t = self.step_next(path, g + 1, bound)

                if t == ResultType.FOUND:
                    return ResultType.FOUND

                if t < min:
                    min = t

                path.pop()

        return min
