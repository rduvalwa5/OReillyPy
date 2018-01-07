#!/usr/local/bin/python3
"""program input_counter.py
   This program breaks input sentences into sets of words and tracks when 
   in order of discovery they were discovered
   """
discovery = 0
setLength = 0
set_s = set([])  # Empty set
dict_d = {}  # Empty dict
sentence = input("Enter text: ")
while len(sentence) > 0: # Test for empty string
  #  list = split the string up and add to list 
  wordList = sentence.split() # split string up into words delimited by white space
#  print(" The List: ", wordList) debug
  for word in wordList:
      set_s.add(word) #list.append but set.add
#      print("The set:", set_s, "Length: ", len(set_s)) debug
      if len(set_s) > setLength:
           discovery += 1
           dict_d[word] = discovery  # add the word as index and value = discovery
           setLength = len(set_s) # increment setLength
#  print(dict_d) debug 
  for word in dict_d:
      print(word, dict_d[word])     # print the index word and value   
  sentence = input("Enter text: ")
print("Finished")