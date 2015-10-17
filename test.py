from unittest import TestCase
import helpers

__author__ = 'Raymond Noonan'


class TestCellName(TestCase):
    def test_return_left_corner(self):
        self.assertEqual("A1", helpers.cell_name(0, 0))
        self.assertEqual("C4", helpers.cell_name(2, 3))

    def test_error_with_neg_values(self):
        self.assertRaises(Exception, helpers.cell_name, -1, 0)
        self.assertRaises(Exception, helpers.cell_name, 0, -1)
        self.assertRaises(Exception, helpers.cell_name, -1, -1)