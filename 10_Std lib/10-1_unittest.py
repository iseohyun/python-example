import unittest


def average(values):
    return sum(values) / len(values)


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)  # test-case 1
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)  # test-case 2
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)


resault = unittest.main()  # Calling from the command line invokes all tests

print(resault)
