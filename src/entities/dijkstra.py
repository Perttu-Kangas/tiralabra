from heapq import heappush, heappop

from util.enums import GridType
from util.coordinates_helper import y_out_of_bounds, x_out_of_bounds


class Dijkstra:

    def __init__(self, ui_logic, grid, start, end):
        self.ui_logic = ui_logic
        self.grid = grid
        self.start = start
        self.end = end

    def find(self):
        heap = []
        dist = {self.start: 0}
        heappush(heap, (0, self.start))

        while len(heap) > 0:
            cur_pos = heappop(heap)[1]
            if cur_pos == self.end:
                return dist.get(cur_pos)

            for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_pos = (cur_pos[0] + move[0], cur_pos[1] + move[1])

                if x_out_of_bounds(self.grid, new_pos[0]) \
                        or y_out_of_bounds(self.grid, new_pos[1]):
                    continue

                if new_pos not in dist:

                    self.ui_logic.draw_rectangle(new_pos[0], new_pos[1], GridType.VISITED)

                    new_dist = dist.get(cur_pos, 0) + 1
                    dist[new_pos] = new_dist
                    heappush(heap, (new_dist, new_pos))
        return -1

    def step(self):
        return -1

    def final_path(self):
        return -1
