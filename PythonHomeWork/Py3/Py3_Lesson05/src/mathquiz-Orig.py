'''
Created on Nov 26, 2013

@author: rduval
'''
# !C:\Python33
import random
from datetime import datetime
import datetime as dt

num = ""
inputMsg = "Input must be a number."
questions = []

def question(num):
        question_num = num
        correct = "wrong"
        b = random.randrange(1, 11)
        a = random.randrange(1, 10)
        print("What is the sum of ", a, "and", b, "?")
        correct_answer = a + b
        start = datetime.now()
        answ = input("Enter Answer: ")
        while not answ.isdigit():
                print(inputMsg)
                answ = input("Enter a Number Answer: ")
        stop = dt.datetime.now()
        if int(answ) == correct_answer:
                correct = "right"
        diff = stop - start
        result = (question_num, correct, diff.seconds, start, stop)
        return result
    
if __name__ == '__main__':
    test_start = datetime.now()
    time_on_q = 0
    for q in range(1, 3):
            r = question(q)
            print(r)
            questions.append(r)
    test_stop = datetime.now()
    total_time = test_stop - test_start
    print(questions)
    for question in questions: 
            print("Question #%s took about %s seconds to complete and was %s." % (question[0], question[2], question[1]))
            # (question[0],question[2],question[1]))
            time_on_q = time_on_q + question[2]
#            print(time_on_q)
    print("You took %s seconds to finish the quiz." % total_time.seconds)
    print("Your average time was %s seconds per question." % float(time_on_q / len(questions)))
    
    


