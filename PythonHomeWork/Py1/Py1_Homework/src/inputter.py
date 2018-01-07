#!/usr/local/bin/python3
""" inputter.py creates a file and then writes to it """

prompt = 'Enter new comments: '
fileName = 'object9.txt'

file =  open(fileName, 'a') # create the file if it does not already exist
file.close() # close so that it can be reopend in append mode
file = open(fileName, 'r')
if file.read() == "":
  print("This file is empty!")
else:
#   print(file.tell()) 
   file.seek(0)
   print('\nExisting contents of this file.')
   print('*' * 30)
   for line in file:
       print(line)
file = open(fileName, 'a')
inp = input(prompt)
while True:
    if inp != "":
       file.write(inp)
       file.close()
       file = open(fileName, 'r')
       for line in file:
          print(line) # print file contents
       file.close()
       file = open(fileName, 'a')
       inp = input(prompt)
    else:
       file.close()
       file = open(fileName, 'r')
       if file.read() == "":
          print("This file is still empty!")
          file.close()
          break
       else:
          file.seek(0)
          print('The contents of this file with any additional contents.')
          print('*' * 53)
          for line in file:
              print(line)
          file.close()
          break