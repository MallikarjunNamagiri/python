import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()


#python -m unittest test_calc.py

