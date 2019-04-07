import unittest

from ClassA_Module import ClassA


class TestClassA(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassA().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassA().returnFalse()
        self.assertFalse(output)


if __name__ == "__main__":
    unittest.main()
