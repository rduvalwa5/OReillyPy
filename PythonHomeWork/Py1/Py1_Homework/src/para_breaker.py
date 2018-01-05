#!/usr/local/bin/python3
""" para_breaker.py  break paragraph into sences delineated by periods and phases delineated by comma. """

text = """We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. - That to
 secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, - That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to a
lter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, wi
ll dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn that mankind are more disposed to suffer, while evils are sufferable than to right thems
elves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is t
heir duty, to throw off such Government, and to provide new Guards for their future security.  - Such has been the patient sufferance of these Colonies; and such is now the necessity which constrains them to alter their former Sy
stems of Government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let F
acts be submitted to a candid world."""

sentence_counter = 0
for sentence in text.split('.'): # since proper syntax for English requires atleast one space after a period
    sentence_counter += 1
    if len(sentence) > 1: # remove the last sentence counted by the last period that has no text following it
       print("Sentence #{0}".format(sentence_counter))
       phrase_counter = 0
       for phrase in sentence.split(','): # correct indention is important in Python
            phrase_counter += 1
            print("Phrase {0:1d}: {1}".format(phrase_counter,phrase.strip())) # strip away leading and lagging spaces
