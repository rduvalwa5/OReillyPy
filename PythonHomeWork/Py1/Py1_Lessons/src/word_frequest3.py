'''
Created on Jul 27, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
""" word_frequency2.py
Count the frequency of each word in a text.
You should see the same results as before. This version of the program uses the same statement to update the count,
even if the word has been seen before. It uses the get() method with a default value of zero to retrieve the existing count, 
so if the word hasn't been seen before, the assignment inserts a value of one against the new key. """
text = """\
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full;
One for the master,
And one for the dame,
And one for the little boy
Who lives down the lane."""

for punc in ",?;.":
    text = text.replace(punc, "")
words = {}

textwords = text.lower().split()
firstword = textwords[0]
for nextword in textwords[1:]:
    if firstword not in words:
          words[firstword] = {}
    words[firstword][nextword] = words[firstword].get(nextword,0)+1
    print(words)
    firstword = nextword
for word in sorted(words.keys()):
       d = words[word]
       for word2 in sorted(d.keys()):
           print(word, ":", word2, d[word2])