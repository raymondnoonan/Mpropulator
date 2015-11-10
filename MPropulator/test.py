from unittest import TestCase
import helpers


class TestCellName(TestCase):
    def test_return_left_corner(self):
        self.assertEqual("A1", helpers.cell_name(0, 0))
        self.assertEqual("C4", helpers.cell_name(3, 2))

    def test_error_with_neg_values(self):
        self.assertRaises(Exception, helpers.cell_name, -1, 0)
        self.assertRaises(Exception, helpers.cell_name, 0, -1)
        self.assertRaises(Exception, helpers.cell_name, -1, -1)


class TestColumnRange(TestCase):
    def test_return_A(self):
        self.assertEqual(['A'], list(helpers.column_range(0, 1)))

    def test_return_multiple(self):
        self.assertEqual(['A', 'B'], list(helpers.column_range(0, 2)))

    def test_skip_columns(self):
        skip_cols = ['A', 'B', 'C', 'D']
        self.assertEqual(['E'], list(helpers.column_range(0, 5, skip_cols)))

    def test_blank_skip_columns(self):
        column_names = ['A', 'B', 'C', 'D', 'E']
        skip_cols = []
        self.assertEqual(column_names, list(helpers.column_range(0, 5,
                                                                 skip_cols)))
