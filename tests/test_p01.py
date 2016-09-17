from python99.p01 import last

import unittest

class P01Test(unittest.TestCase):

    def test_last_element(self):
        l = [1, 2, 3, 4]
        self.assertEqual(last(l), 4)

if __name__ == '__main__':
    unittest.main()
