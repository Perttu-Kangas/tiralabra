from heapq import heappush, heappop

from util.enums import GridType, ResultType
from util.coordinates_helper import y_out_of_bounds, x_out_of_bounds
from util.heap import heappush, heappop


class Dijkstra:

    def __init__(self, grid, start, end, draw=None):
        self.grid = grid
        self.start = start
        self.end = end
        self.draw = draw
        self.final_path = None

        # Init
        self.heap = []
        self.dist = {self.start: (0, None)}
        heappush(self.heap, (0, self.start))

    def step(self):
        if not self.heap:
            self.final_path = ResultType.NOT_FOUND
            return

        cur_pos = heappop(self.heap)[1]
        if cur_pos == self.end:
            self.final_path = self.get_final_path(), self.dist.get(cur_pos)[0]
            return

        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (cur_pos[0] + move[0], cur_pos[1] + move[1])

            if x_out_of_bounds(self.grid, new_pos[0]) \
                    or y_out_of_bounds(self.grid, new_pos[1]):
                continue

            if self.grid[new_pos[1]][new_pos[0]] == GridType.WALL:
                continue

            if new_pos not in self.dist:

                if self.draw:
                    self.draw(new_pos[0], new_pos[1], GridType.VISITED)

                new_dist = self.dist.get(cur_pos, 0)[0] + 1
                self.dist[new_pos] = (new_dist, cur_pos)
                heappush(self.heap, (new_dist, new_pos))

    def get_final_path(self):
        path = []
        xy = self.end

        while xy:
            path.append(xy)
            xy = self.dist.get((xy[0], xy[1]))[1]

        path.reverse()

        return path
