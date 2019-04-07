import unittest

from ..ClassG_Module import ClassG

# from tests_package.internal_package.ClassG_Module import ClassG


class TestClassG(unittest.TestCase):

    def test_returnTrue(self):
        output = ClassG().returnTrue()
        self.assertTrue(output)

    def test_returnFalse(self):
        output = ClassG().returnFalse()
        self.assertFalse(output)

if __name__ == "__main__":
    unittest.main()
