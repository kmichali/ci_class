import unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit test". Tests on 1 and 2.
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.assertTrue(IsOdd(1))

    def testTwo(self):
        self.assertFalse(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()

