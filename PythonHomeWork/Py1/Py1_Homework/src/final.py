'''
Created on Jul 4, 2014

@author: rduvalwa2
'''#!/usr/local/bin/python3
"""Lesson 16 Objective 2 and 3 final.py"""
import sys

def open_read_only(file_name):
        """ Open file in read only mode and exit if file does not exist """
        try:
                f = open(file_name, 'r')
                return f
        except IOError:
                print ('There is no file named', file)
                sys.exit()

def word_len(word):
        """ Open file in read only mode and exit if file does not exist """
        unChars = [',','.','?','!','@','#','$','%','^','&','*','(',')','+','=','{','}','[',']','|','\\','/',':',';','\'', '-']
        count = 0
        for ch in word:
                if ch not in unChars:
                        count += 1
        return count

def print_length_count(dict):
                print(" Length Count")
                for length in sorted(dict.keys()):
                        print(" {0} {1}".format(length ,dict[length]))

# returns the hightest value from the dict
def get_max(dic):
        max = 0
        for ke in dic.keys():
                if dic[ke] > max:
                                max = dic[ke]
        max = round(max/100) * 100
        return max

#caluclate number of rows
def get_num_rows(max_val,row_val):
                return round(max_val/row_val)


if __name__ == "__main__":
        try:
                file = sys.argv[1]
        except IndexError:
                print("Syntax final.py <input file name>")
                sys.exit()

length_counts = {}
readFile = open_read_only(file)
for line in readFile:
        for word in line.split():
                length = word_len(word)
                if length > 0:
                        if length in length_counts:
                                length_counts[length] += 1
                        else:
                                length_counts[length] = 1
print_length_count(length_counts)
readFile.close()

#set value of each row this could be done by passing an argument
row_val = 10

#max_value is the highest value in the dict.  this is used to calcuation the number of rows to print
max_val = get_max(length_counts)

#get the number of rows
row_count = get_num_rows(max_val,row_val)

#number of columns
col_count = len(length_counts)

# store the printable row strings 
rows = {}
#Store the string for a column
columns = []
for r in range(1,row_count + 1):
                for col in range(1,col_count + 1):
                        if length_counts[col] > row_val:
                                        columns.append('***')
                        else:
                                columns.append('   ')
                row_val += 10
                rows[r] = "".join(columns)
                columns = []

#label_row is used to determine when to apply a label
label_row = 1

#provide line break
print("")

#print the chart rows
for row in range( 1, len(rows) + 1):
        label = row_val - 10
        if label_row == row:
                        if len(str(label)) < 3:
#                               print(" {0}-|{1}".format(label,rows[c - row]))   
                                print(" {0}-|{1}".format(label,rows[(len(rows) + 1) - row]))
                        else:
                                print("{0}-|{1}".format(label,rows[(len(rows) + 1)  - row]))
                        row_val = row_val - 10
                        label_row = label_row + 5
        else:
                        print("{0}-|{1}".format("   ",rows[(len(rows) + 1)  - row]))
                        row_val = row_val - 10

# create the chart base line
base_line = ['  0 ']
for item in range( 1, len(length_counts) + 1):
                        base_line.append('-+-')

#print the chart base line
print(''.join(base_line))

#create the chart base labels
base_labels = ['    ']
for itm in length_counts.keys():
                if itm < 10:
                        base_labels.append('  {0}'.format(itm))
                if itm > 9:
                        base_labels.append(' {0}'.format(itm))

#print chart base labels
print(''.join(base_labels))
                    
