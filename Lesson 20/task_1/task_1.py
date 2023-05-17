# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.
import unittest
import module_to_test


class NameTestCase(unittest.TestCase):
    def test_make_operation(self):
        result = module_to_test.make_operation('+', 7, 8)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
