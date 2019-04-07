import unittest
from classes_package.ClassC_Module import ClassC


class TestClassC(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassC().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassC().returnFalse()
        self.assertFalse(output)


if __name__ == "__main__":
    unittest.main()
