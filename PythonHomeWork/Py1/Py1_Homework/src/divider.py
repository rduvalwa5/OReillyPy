#!/usr/local/bin/python3
"""divider.py exception catching"""

prompt = "Input an interger: "
while True:
        inp = input(prompt)
        if inp == "":
                        break
        try:
                a = int(inp)
                print(10/int(inp))
        except ValueError:
                        print("Your input must be an integer.")
                        inp = ""
        except ZeroDivisionError:
                        print("Your input must not be zero (0)")
                        inp = ""
