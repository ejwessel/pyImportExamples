import unittest

from .internal_package.ClassF_Module import ClassF


class TestClassF(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassF().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassF().returnFalse()
        self.assertFalse(output)

if __name__ == "__main__":
    unittest.main()
