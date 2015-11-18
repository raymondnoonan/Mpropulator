import unittest
import validations as vd
        
class TestValidateInput(unittest.TestCase):
    
class TestValidateConfigPath(unittest.TestCase):
    
class TestValidateConfigRead(unittest.TestCase):
    
class TestValidateTabs(unittest.TestCase):
    
class TestValidateCellname(unittest.TestCase):
    def test_edge_cells(self):
        self.assertEqual(vd.validate_cellname("A1"), True)
        self.assertEqual(vd.validate_cellname("ZZ999"), True)
        self.assertRaises(ValueError, vd.validate_cellname, "1A")
        self.assertRaises(ValueError, vd.validate_cellname, "AAA1")
        
class TestValidateSkiprows(unittest.TestCase):
    def test_good_skiprows(self):
        self.assertEqual(vd.validate_skiprows([]), True)
        self.assertEqual(vd.validate_skiprows([2]), True)
        self.assertEqual(vd.validate_skiprows([3,5]), True)
        
    def test_bad_skiprows(self):
        self.assertRaises(ValueError, vd.validate_skiprows, ["A"])
        self.assertRaises(ValueError, vd.validate_skiprows, [2, "A"])
    
class TestValidateSkipcols(unittest.TestCase):
    def test_good_skipcols(self):
        self.assertEqual(vd.validate_skipcols([]), True)
        self.assertEqual(vd.validate_skipcols(["A"]), True)
        self.assertEqual(vd.validate_skipcols(["a"]), True)
        self.assertEqual(vd.validate_skipcols(["ZZ"]), True)
        self.assertEqual(vd.validate_skipcols(["B", "C"]), True)
        
    def test_bad_skipcols(self):
        self.assertRaises(ValueError, vd.validate_skipcols, [1])
        self.assertRaises(ValueError, vd.validate_skipcols, ["AAA"])
        self.assertRaises(ValueError, vd.validate_skipcols, ["aaa"])
        self.assertRaises(ValueError, vd.validate_skipcols, ["Z", "AAA"])
        self.assertRaises(ValueError, vd.validate_skipcols, [1, "A"])
        
class TestValidateIgnore(unittest.TestCase):
    def test_ignore_vals(self):
        self.assertEqual(vd.validate_ignore("True"), True)
        self.assertEqual(vd.validate_ignore("False"), True)
        self.assertRaises(ValueError, vd.validate_ignore, "")
        self.assertRaises(ValueError, vd.validate_ignore, " ")
        self.assertRaises(ValueError, vd.validate_ignore, "yes")
    
class TestValidateConfig(unittest.TestCase):
    
if __name__ == "__main__":
    unittest.main()
