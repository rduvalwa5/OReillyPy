#!/usr/local/bin/python3
""" guess.py
    give user 5 chances to guess the secret value """

import random
secret = random.randint(1,20)
# print(secret)  debugging
chances = 5
guess = 0
while guess < chances:
#   print("Guess is ", guess)  debugging
   print("You have ", chances - guess," tries left")
   pick = int(input("Pick a number between 1 and 20: "))
   while pick < 1 or pick > 20:
       print("Your pick ", pick,"is out of range")
       pick = int(input("Pick a number between 1 and 20: "))
   if pick == secret:
      print("Correct! Well done, the number was", secret)
      break
   elif pick > secret:
      guess += 1
      print("Guess lower")
   elif pick < secret:
      guess += 1
      print("Guess higher")
if guess == chances:
   print("The secret number was ", secret, " and you are out of ", chances, "chances")
