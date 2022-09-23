import unittest
from util.coordinates_helper import *
from util.enums import GridType


class TestSnake(unittest.TestCase):
    def setUp(self):
        grid_rows = 5
        grid_cols = 8
        self.grid = [[GridType.NONE] * grid_rows] * grid_cols

    def test_x_out_of_bounds_left(self):
        self.assertEqual(x_out_of_bounds(self.grid, 0), False)
        self.assertEqual(x_out_of_bounds(self.grid, -1), True)

    def test_x_out_of_bounds_right(self):
        self.assertEqual(x_out_of_bounds(self.grid, 4), False)
        self.assertEqual(x_out_of_bounds(self.grid, 5), True)

    def test_y_out_of_bounds_up(self):
        self.assertEqual(y_out_of_bounds(self.grid, 0), False)
        self.assertEqual(y_out_of_bounds(self.grid, -1), True)

    def test_y_out_of_bounds_down(self):
        self.assertEqual(y_out_of_bounds(self.grid, 7), False)
        self.assertEqual(y_out_of_bounds(self.grid, 8), True)

    def test_normalize(self):
        self.assertEqual(normalize(25, 51), 2)
        self.assertEqual(normalize(25, 49), 1)
        self.assertEqual(normalize(25, 50), 2)
