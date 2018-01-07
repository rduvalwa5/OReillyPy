#!/usr/local/bin/python3
"""caser.py"""
import sys

def apply_caps(text):
        converted = text.capitalize()
        print(converted)

def apply_title(text):
        converted = text.title()
        print(converted)

def make_upper(text):
        converted = text.upper()
        print(converted)

def make_lower(text):
        converted = text.lower()
        print(converted)

def quit():
        """ Terminates the program."""
        print("Goodbye for now!")
        sys.exit()

if __name__ == "__main__":
   switch = {
        'caps': apply_caps,
        'title': apply_title,
        'upper': make_upper,
        'lower': make_lower,
        'exit': quit
    }

options = switch.keys()
prompt = 'Enter a function name({0}): '.format(', '.join(options))
while True:
   inp = input(prompt)
   option = switch.get(inp, None)
   if inp == 'exit':
       switch[inp]()
   else:
       if option:
          text = input("Input text: ")
          switch[inp](text)
       else:
          print('Please select a valid option!')
