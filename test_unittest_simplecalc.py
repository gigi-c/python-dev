from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
    cal = SimpleCalc() # create an object

    def test_add(self):
        self.assertEqual(self.cal.add(2, 4), 6) # assertEqual means does LHS [add(2,4)] equal to RHS [6]

    def test_substract(self):
        self.assertEqual(self.cal.substract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.cal.divide(6, 2), 3)


if __name__ == '__main__': # this file becomes the main file (more important than the import file)
    unittest.main()

# to run each individual test
# --> right click open terminal
# --> python -m unittest -v