#!/usr/local/bin/python3

"""secret_code.py
   this code uses simple encoding, adding 1 to the original ordinal values of the input letter for the output
   and making that the output value. The output string is then reversed """
debug = False
user_input = input('Enter text: ')
user_output = []
r_out = []

for letter in user_input:
    num_out = ord(letter)+1
    user_output.append(chr(num_out))
print("Input was: " + user_input)

if debug:
   mystring = "".join(user_output)
   print(mystring)
   for i in reversed(user_output):
        r_out.append(i)
   rev_string = "".join(r_out)
else:
   for i in reversed(user_output):
        r_out.append(i)
   rev_string = "".join(r_out)

print(rev_string)

