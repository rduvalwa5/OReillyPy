#!/usr/bin/python3
#
#check_string.py
#
s = input("Please enter an upper-case string ending with a period: ")
# check for upper can and ends with period
if s.isupper() and s.endswith("."):
  print("Input meets both requirements")
# check for all upper case if not upper case dont care about period
elif not s.isupper():
  print("Input is not all upper case.")
# check if all upper the string ends in a period
elif s.isupper() and not s.endswith("."):
  print("Input does not end with a period.")