import unittest
from services.ui_logic import UILogic
from util.enums import GridType


class TestUILogic(unittest.TestCase):
    def setUp(self):
        self.ui_logic = UILogic()

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
