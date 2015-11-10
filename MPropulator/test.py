import unittest
import helpers


class TestCellName(unittest.TestCase):
    def test_return_left_corner(self):
        self.assertEqual("A1", helpers.cell_name(0, 0))
        self.assertEqual("C4", helpers.cell_name(3, 2))

    def test_error_with_neg_values(self):
        self.assertRaises(Exception, helpers.cell_name, -1, 0)
        self.assertRaises(Exception, helpers.cell_name, 0, -1)
        self.assertRaises(Exception, helpers.cell_name, -1, -1)


class TestColumnRange(unittest.TestCase):
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


class TestColToNumber(unittest.TestCase):
    def test_return_basic(self):
        self.assertEqual(0, helpers.col_to_number("A"))

    def test_return_multi(self):
        self.assertEqual(27, helpers.col_to_number("AB"))

    def test_handle_blank(self):
        pass

    def test_not_letters(self):
        self.assertRaises(ValueError, helpers.col_to_number("B45C"))

    def test_handle_space(self):
        self.assertRaises(ValueError, helpers.col_to_number("A  B"))

    def test_handle_leading_space(self):
        self.assertRaises(ValueError, helpers.col_to_number(" AB"))

if __name__ == "__main__":
    unittest.main()
