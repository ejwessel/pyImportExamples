import unittest

from ClassA_Module import staticMethod

class TestClassA(unittest.TestCase):

    def test_static(self):
        output = staticMethod()
        self.assertTrue(output)

if __name__ == "__main__":
    unittest.main()
