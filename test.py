from unittest import TestCase
import helpers

__author__ = 'Raymond Noonan'


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

    def test_return_incremented(self):
        self.assertEqual(['A', 'C'], list(helpers.column_range(0, 3, chunk=1,
                                                               skip=1)))

    def test_return_multi_incremented(self):
        self.assertEqual(['A', 'C', 'E'], \
                         list(helpers.column_range(0, 5, chunk=1, skip=1)))

    def test_return_super_incremented(self):
        self.assertEqual(['A', 'AA'], \
                         list(helpers.column_range(0, 27, chunk=1, skip=25)))

    def test_chunk_works(self):
        test_list = ['A', 'B', 'C', 'E', 'F', 'G', 'I', 'J', 'K', 'M', 'N', 'O']
        self.assertEqual(test_list, list(helpers.column_range(0, 15, chunk=3, \
                                                   skip=1)))