import unittest

from entities.dijkstra import Dijkstra
from util.enums import GridType, ResultType


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # 5x5 grid

        self.grid = [[GridType.NONE for _ in range(5)] for _ in range(5)]

        self.grid[0][1] = GridType.START
        self.grid[3][3] = GridType.END

        self.grid[0][2] = GridType.WALL
        self.grid[1][2] = GridType.WALL
        self.grid[2][2] = GridType.WALL
        self.grid[3][2] = GridType.WALL

        self.dijkstra = Dijkstra(self.grid, (1, 0), (3, 3))

        # N S W N N
        # N N W N N
        # N N W N N
        # N N W E N
        # N N N N N

    def test_path_and_distance(self):
        while not self.dijkstra.final_path:
            self.dijkstra.step()

        self.assertEqual(self.dijkstra.final_path[0], [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 3)])
        self.assertEqual(self.dijkstra.final_path[1], 7)

    def test_not_found(self):
        self.grid[4][2] = GridType.WALL
        while not self.dijkstra.final_path:
            self.dijkstra.step()

        self.assertEqual(self.dijkstra.final_path, ResultType.NOT_FOUND)
