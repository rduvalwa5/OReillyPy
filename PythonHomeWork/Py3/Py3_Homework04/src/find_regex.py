'''
Created on Jun 30, 2013
Instructions:
 1. Create a Python3_Homework04 project and assign it to your Python3_Homework working set. 
 2. Create a program named find_regex.py 
    a. takes the following text and finds the start and end positions of the phrase, "Regular Expressions"
 3. Text to use in find_regex.py
    In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language 
    theoryin a set of models using a notation called "regular sets" as a method to do pattern matching. 
    Activeusage of this system, called Regular Expressions, started in the 1960s and continued under 
    such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.
 4. Your project should meet the following conditions:
    Your code must return 231 as the start and 250 as the end. 
    You must include a separate test_find_regex.py program that confirms that your code functions as instructed.
@author: rduvalwa2
'''
def find_regex():
    
    import re
    pat = "Regular Expressions"
    txt = "In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called \"regular sets\" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer."
    mat = re.search(pat, txt)
    return mat.start, mat.end

if __name__ == "__main__":
    start, end = find_regex()
    import unittest
    class TestFind_Regex(unittest.TestCase):
        def test_start_end(self):
            self.assertEqual(231, start())
            self.assertEqual(250, end())

    unittest.main()
