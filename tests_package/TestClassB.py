import unittest

from ClassB_Module import ClassB

class TestClassB(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassB().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassB().returnFalse()
        self.assertFalse(output)


if __name__ == "__main__":
    unittest.main()
