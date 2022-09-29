import unittest
from tkinter import Event

from services.ui_logic import UILogic
from util.enums import GridType


class TestUILogic(unittest.TestCase):
    def setUp(self):
        # 4x4 grid
        self.ui_logic = UILogic(100, 100, 25)
        self.ui_logic.draw_rectangle = self.draw_rectangle

    def draw_rectangle(self, x, y, grid_type):
        # dummy test method
        return

    def test_init_grid(self):
        for y in range(len(self.ui_logic.grid)):
            for x in range(len(self.ui_logic.grid[y])):
                self.assertEqual(self.ui_logic.grid[y][x], GridType.NONE)

    def test_modified_grid(self):
        tk_event = Event()
        tk_event.x = 5
        tk_event.y = 5
        self.ui_logic.handle_motion(tk_event)

        tk_event.x = 98
        tk_event.y = 75
        self.ui_logic.handle_motion(tk_event)

        tk_event.x = 74
        tk_event.y = 56
        self.ui_logic.handle_motion(tk_event)

        tk_event.x = 0
        tk_event.y = 27
        self.ui_logic.current_type = GridType.START
        self.ui_logic.handle_motion(tk_event)

        tk_event.x = 75
        tk_event.y = 0
        self.ui_logic.current_type = GridType.END
        self.ui_logic.handle_motion(tk_event)

        # W N N E
        # S N N N
        # N N W N
        # N N N W

        # Test like this because had lovely Python experience
        # Apparently this makes list which uses same references:
        # [[GridType.NONE] * grid_rows] * grid_cols
        # But this makes new references (and is now used when creating grid):
        # [[GridType.NONE for _ in range(grid_cols)] for _ in range(grid_rows)]
        for y in range(len(self.ui_logic.grid)):
            for x in range(len(self.ui_logic.grid[y])):
                if (x == 0 and y == 0) or (x == 2 and y == 2) or (x == 3 and y == 3):
                    self.assertEqual(self.ui_logic.grid[y][x], GridType.WALL)
                elif x == 3 and y == 0:
                    self.assertEqual(self.ui_logic.grid[y][x], GridType.END)
                elif x == 0 and y == 1:
                    self.assertEqual(self.ui_logic.grid[y][x], GridType.START)
                else:
                    self.assertEqual(self.ui_logic.grid[y][x], GridType.NONE)

    def test_handle_motion(self):
        tk_event = Event()
        tk_event.x = 5
        tk_event.y = 5
        self.ui_logic.handle_motion(tk_event)
        self.assertEqual(self.ui_logic.grid[0][0], GridType.WALL)

    def test_change_start(self):
        self.ui_logic.current_type = GridType.START
        self.ui_logic.change_start(1, 2)
        self.assertEqual(self.ui_logic.grid[2][1], GridType.START)
        self.assertEqual(self.ui_logic.start_position, (1, 2))

        self.ui_logic.change_start(0, 0)
        self.assertEqual(self.ui_logic.grid[2][1], GridType.NONE)
        self.assertEqual(self.ui_logic.grid[0][0], GridType.START)
        self.assertEqual(self.ui_logic.start_position, (0, 0))

    def test_change_end(self):
        self.ui_logic.current_type = GridType.END
        self.ui_logic.change_end(1, 2)
        self.assertEqual(self.ui_logic.grid[2][1], GridType.END)
        self.assertEqual(self.ui_logic.end_position, (1, 2))

        self.ui_logic.change_end(0, 0)
        self.assertEqual(self.ui_logic.grid[2][1], GridType.NONE)
        self.assertEqual(self.ui_logic.grid[0][0], GridType.END)
        self.assertEqual(self.ui_logic.end_position, (0, 0))

    def test_init_type(self):
        self.assertEqual(self.ui_logic.current_type, GridType.WALL)

    def test_wall_type_change(self):
        self.ui_logic.start_type()
        self.ui_logic.wall_type()
        self.assertEqual(self.ui_logic.current_type, GridType.WALL)

    def test_start_type_change(self):
        self.ui_logic.start_type()
        self.assertEqual(self.ui_logic.current_type, GridType.START)

    def test_end_type_change(self):
        self.ui_logic.end_type()
        self.assertEqual(self.ui_logic.current_type, GridType.END)
