import unittest


class TestInit(unittest.TestCase):
    def testinit(self):
        import __init__
        # if init import properly, then passes
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
