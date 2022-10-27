import unittest

import random
from entities.dijkstra import Dijkstra
from entities.idastar import IDAStar
from util.enums import GridType, ResultType


class TestCorrectness(unittest.TestCase):

    def test_correctness(self):

        # 3 tests
        for i in range(3):
            # 10x10 grid
            grid = [[GridType.NONE for _ in range(10)] for _ in range(10)]

            # Start and end can be at same location
            start = (random.randint(0, 9), random.randint(0, 9))
            end = (random.randint(0, 9), random.randint(0, 9))

            grid[start[1]][start[0]] = GridType.START
            grid[end[1]][end[0]] = GridType.END

            idastar = IDAStar(grid, start, end)
            dijkstra = Dijkstra(grid, start, end)

            while not idastar.final_path:
                idastar.step()

            while not dijkstra.final_path:
                dijkstra.step()

            # Check that they found same distance, path may differ
            self.assertEqual(dijkstra.final_path[1], idastar.final_path[1])

    def test_correctness_with_walls(self):
        # 3 tests
        for i in range(3):
            # 10x10 grid
            grid = [[GridType.NONE for _ in range(10)] for _ in range(10)]

            # Start and end can be at same location
            start = (random.randint(0, 9), random.randint(0, 9))
            end = (random.randint(0, 9), random.randint(0, 9))

            grid[start[1]][start[0]] = GridType.START
            grid[end[1]][end[0]] = GridType.END

            # 30 random walls
            for j in range(30):
                wall_pos = (random.randint(0, 9), random.randint(0, 9))
                if wall_pos != start and wall_pos != end:
                    grid[wall_pos[1]][wall_pos[0]] = GridType.WALL

            idastar = IDAStar(grid, start, end)
            dijkstra = Dijkstra(grid, start, end)

            while not idastar.final_path:
                idastar.step()

            while not dijkstra.final_path:
                dijkstra.step()

            if dijkstra.final_path == ResultType.NOT_FOUND or idastar.final_path == ResultType.NOT_FOUND:
                # If not found, you can't take 2 arg on assert equal
                self.assertEqual(dijkstra.final_path, idastar.final_path)
            else:
                # Check that they found same distance, path may differ
                self.assertEqual(dijkstra.final_path[1], idastar.final_path[1])
