'''
Created on Oct 28, 2012
@author: rduval
high_score.py
function that keeps players high scores in a shelve persistence
'''

import shelve

def high_score(player, score):
    dataBase = 'scores'
    shelf = shelve.open(dataBase)
    if player in shelf:
        if score > shelf[player]:
            shelf[player] = score
    else:
        shelf[player] = score
    return shelf[player]
    shelf.close()
