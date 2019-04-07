import unittest

from classes_package.ClassD_Module import ClassD


class TestClassD(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassD().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassD().returnFalse()
        self.assertFalse(output)

if __name__ == "__main__":
    unittest.main()
