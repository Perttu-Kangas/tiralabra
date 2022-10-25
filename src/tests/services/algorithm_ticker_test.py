import unittest
from tkinter import Event

from entities.dijkstra import Dijkstra
from entities.idastar import IDAStar
from services.algorithm_ticker import AlgorithmTicker
from services.ui_logic import UILogic
from util.enums import GridType


class TestAlgorithmTicker(unittest.TestCase):
    def setUp(self):
        # 4x4 grid
        self.ui_logic = UILogic(4, 4, 1)
        self.ui_logic.draw_rectangle = self.draw_rectangle
        self.mock = 0
        self.mock_list = []
        self.ticker = AlgorithmTicker(self.ui_logic, self.ui_logic.grid,
                                      IDAStar(self.ui_logic.grid, (0, 0), (3, 3), draw=self.draw_rectangle),
                                      step_interval=0)

    def draw_rectangle(self, x, y, grid_type):
        # dummy test method
        self.mock_list.append((x, y))
        self.mock += 1
        return

    def test_start_ticker(self):
        self.ticker.start_ticker()
        self.assertNotEqual(self.ticker.time_in_ns, 0)
        self.assertEqual(self.ticker.visits, 8)
        self.assertEqual(self.ticker.algorithm.final_path, ([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)],
                                                            6))

    def test_instant_find(self):
        self.ticker.instant_find(2)
        self.assertEqual(self.ticker.algorithm.draw, None)
        self.assertNotEqual(self.ticker.time_in_ns, 0)
        self.assertEqual(self.ticker.visits, 16)  # 16 because looping 2 times
        self.assertEqual(self.ticker.algorithm.final_path, ([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)],
                                                            6))

    def test_get_time_in_ms(self):
        self.ticker.time_in_ns = 1000000
        self.assertEqual(self.ticker.get_time_in_ms(), 1)

    def test_get_distance(self):
        self.ticker.algorithm.final_path = [(0, 0), (0, 1), (0, 2)], 2
        self.assertEqual(self.ticker.get_distance(), 2)

    def test_get_distance_not_exist(self):
        self.assertEqual(self.ticker.get_distance(), -1)

    def test_draw_at(self):
        self.ticker.draw_at(0, 0, GridType.WALL)
        self.assertEqual(self.mock_list, [(0, 0)])
        self.assertEqual(self.mock, 1)

    def test_draw_path(self):
        path = [(0, 0), (0, 1), (0, 2)]
        self.ticker.draw_path([(0, 0), (0, 1), (0, 2)], GridType.WALL)
        self.assertEqual(self.mock_list, path)
        self.assertEqual(self.mock, 3)

    def test_reset_grid(self):
        self.ticker.reset_grid()
        self.assertEqual(self.mock, 16)

    def test_new_visit(self):
        self.ticker.new_visit()
        self.assertEqual(self.ticker.visits, 1)
