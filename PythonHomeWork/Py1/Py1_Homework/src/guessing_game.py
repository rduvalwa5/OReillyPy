#!/usr/local/bin/python3
""" guessing_game.py """

import random
answer = random.randint(1,99)
guess = "0"
while int(guess) != answer:
   guess = input("Pick a number between 1 and 99: ")
   if guess == "" or guess.isalpha():
       guess = "0"
   if int(guess) == answer:
      print("You guessed it!")
   elif int(guess) > answer:
      print("Guess lower")
   elif int(guess) < answer:
      print("Guess higher")
