#!/usr/local/bin/python3
""" pair_frequency2.py
"""
text = """\
What, what, sheep, dip, what, sheep dip dip dip
Have you what what what what have you have"""

for punc in ",?;.":
    text = text.replace(punc, "")
words = {}
textwords = text.lower().split()
firstword = textwords[0]
for nextword in textwords[1:]:
    if firstword not in words:
          words[firstword] = {}
    words[firstword][nextword] = words[firstword].get(nextword,0)+1
    print("For first word ", firstword, "and nextword ", nextword, "\n", words)
    firstword = nextword
for word in sorted(words.keys()):
       d = words[word]
       for word2 in sorted(d.keys()):
           print(word, ":", word2, d[word2])