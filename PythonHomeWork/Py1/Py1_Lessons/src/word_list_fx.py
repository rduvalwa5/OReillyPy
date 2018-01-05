'''
Created on Jul 28, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""word_list.py
   this program prints out words from input that separates the 
   words by whether they contain a capital letter or not then prints the words
   The words with capital letters are printed 1st. """
words_upper = []  #store capital letter words
words_lower = []     #store non capital letter words
words = input("Enter a list of words: ")
word_list = words.split() #create a list of words by split on space 
for word in word_list:
     if word.islower():  #test for only lower case letters
         words_lower.append(word)  # put lower case words in words_lower
     else:
         words_upper.append(word)  # put lower case words in words_upper
recombined_words = (words_upper + words_lower) # 
# print(recombined_words) debug       
for word in recombined_words:
     print(word)