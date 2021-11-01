import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_Add(self):
        result = calc.add(10, 5)
        self.assertEqual(15, result)

if __name__ == '__main__':
    unittest.main()

