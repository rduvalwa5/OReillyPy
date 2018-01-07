'''
Created on Jun 30, 2013

@author: rduvalwa2
'''

import unittest
from find_regex import find_regex

class TestFind_Regex(unittest.TestCase):
    """
    Test the match object start position is 231
    """
    def test_start_end(self):
            start, end = find_regex()
            self.assertEqual(231, start(), "Start did not match expect position value 231")
            self.assertEqual(250, end(), "End did not match expected position value 250")

if __name__ == "__main__":
    unittest.main()

