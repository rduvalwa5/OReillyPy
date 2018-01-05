'''
Created on Nov 27, 2013
@author: rduval
'''
import unittest
from mathquiz import mathQuestion
from datetime import datetime

class TestMathquiz(unittest.TestCase):
# this test requires user interaction    
        def test_question(self):
            testTime = datetime.now()
            int1 = 10
            int2 = 9
            answer = int1 + int2            
            quest, correctAnswer, start = mathQuestion(int1, int2)
            self.assertEquals("What is the sum of 10 and 9?", quest, "Question is wrong")
            self.assertEquals(answer, correctAnswer, "Correct answer is not correct")
            self.assertLess(testTime, start)
