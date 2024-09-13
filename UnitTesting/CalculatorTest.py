from Calculator import *
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add_one_and_one(self):
        r = self.calc.add(1,1)
        self.assertEqual(r, 2, 'one plus one is two')

    def test_sub_two_and_one(self):
        r = self.calc.sub(2,1)
        self.assertEqual(r, 1, 'two minus one is one')

    def test_mult_two_and_one(self):
        r = self.calc.mult(3,7)
        self.assertEqual(r, 21, 'three * seven is twenty one')

    def test_div_two_and_one(self):
        r = self.calc.div(30,2)
        self.assertEqual(r, 15, 'thirty / two is fifteen')

    def test_div_two_and_zero(self):
        # self.assertRaises(ZeroDivisionError, lambda: self.calc.div(5, 0))
        with self.assertRaises(ZeroDivisionError, msg="Cannot divide by zero"):
            self.calc.div(2, 0)

    def test_memory_store(self):
        self.calc.add(8, 3)
        self.assertEqual(self.calc.memory, 11)

    def test_memory_clear(self):
        self.calc.add(2, 3)
        self.calc.cleanMemory()
        self.assertIsNone(self.calc.memory)

if __name__ == '__main__':
    unittest.main()