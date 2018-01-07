'''
Created on Dec 2, 2013
@author: rduvalwa2
'''
import random
from datetime import datetime

num = ""
questions = []

def mathQuestion(x, y):
        q_start = getStartTime()
        question = "What is the sum of " + str(x) + " and " + str(y) + "?"
        correct_answer = x + y
        return (question, correct_answer, q_start)
            
def getAnswer(num, correct_answer, q_start):
    correct = "wrong"
    answer = input("Enter Answer: ")
    while not answer.isdigit():
            print("Input must be a number.")
            answer = input("Enter a Number Answer: ")
    q_stop = getStopTime()
    if int(answer) == correct_answer:
            correct = "right"
    diff = q_stop - q_start
    result = (num, correct, diff.seconds)
    return result

            
def getStartTime():
        startTime = datetime.now()
        return startTime

def getStopTime():
        stopTime = datetime.now()
        return stopTime    

def calculateTotalTime(testStart, testEnd):
        total_time = testEnd - testStart
        return total_time.seconds
 
def printOutPut(totalTime): 
        for question in questions: 
            print("Question #%s took about %s seconds to complete and was %s." % (question[0], question[2], question[1]))
        print("You took %s seconds to finish the quiz." % totalTime)
        print("Your average time was %s seconds per question." % float(totalTime / len(questions)))

if __name__ == '__main__':
    test_start = datetime.now()
    for n in range(1, 6):
            int1 = random.randrange(1, 11)
            int2 = random.randrange(1, 11)            
            quest, correctAnswer, start = mathQuestion(int1, int2)
            print(type(start))
            print(quest)
            result = getAnswer(n, correctAnswer, start)
            questions.append(result)
    test_stop = datetime.now()
    total_time = test_stop - test_start
    calculateTotalTime(test_start, test_stop)
    printOutPut(total_time.seconds)
