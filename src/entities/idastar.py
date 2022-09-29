from util.enums import GridType
from util.coordinates_helper import y_out_of_bounds, x_out_of_bounds, manhattan


class IDAStar:

    def __init__(self, ui_logic, grid, start, end):
        self.ui_logic = ui_logic
        self.grid = grid
        self.start = start
        self.end = end

    def find(self):
        bound = manhattan(self.start, self.end)
        path = [self.start]

        # Temp id ( will be enum )
        # t == -5 = found
        # t == 99999 ( return -3 ) = not found

        while True:
            t = self.step(path, 0, bound)
            if t == -5:

                for z in path:
                    self.ui_logic.draw_rectangle(z[0], z[1], GridType.VISITED)

                return path, bound
            if t == 99999:
                return -3
            bound = t

    def step(self, path, g, bound):
        node = path[-1]
        f = g + manhattan(node, self.end)

        if f > bound:
            return f

        if node == self.end:
            return -5

        min = 99999

        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (node[0] + move[0], node[1] + move[1])

            if x_out_of_bounds(self.grid, new_pos[0]) \
                    or y_out_of_bounds(self.grid, new_pos[1]):
                continue

            if self.grid[new_pos[1]][new_pos[0]] == GridType.WALL:
                continue

            if new_pos not in path:

                path.append(new_pos)
                t = self.step(path, g + 1, bound)
                if t == -5:
                    return -5

                if t < min:
                    min = t

                path.pop()

        return min

    def final_path(self):
        return -1
