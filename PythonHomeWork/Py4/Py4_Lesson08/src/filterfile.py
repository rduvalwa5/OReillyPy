'''
Created on Mar 10, 2014
Filter file contents using a sequence of generators
@author: rduvalwa2
'''
def nocomment(f):
    "Generate the non-comment lines of a file."
    for line in f:
        if not line.startswith("#"):
            yield line
            
def nospaces(f):
    "Generate the lines of a file without leading or trailing spaces."
    for line in f:
            yield line.strip()
        
def noblanks(f):
    "Generate the non-blank lines of file."
    for line in f:
        if line:
            yield line
            
if __name__ == "__main__":
    "Note that the order in which the functions are stacked impacts the output"
    print("This is the expected order.")
    for line in nocomment(noblanks(nospaces(open("py08-01.txt")))):
        print(line)
    print("--" * 8)
    print("This printed blank lines and a comment")
    for line in nospaces(nocomment(noblanks(open("py08-01.txt")))):
        print(line)
    print("--" * 8)
    print("This printed a commented line")
    for line in noblanks(nospaces(nocomment(open("py08-01.txt")))):
        print(line)

'''
This line should be the first of four lines in the output
And this should be the second
This should be the third line of output
And this should be the last.
----------------


This line should be the first of four lines in the output

And this should be the second

# This should not appear (leading spaces but a comment)
This should be the third line of output

And this should be the last.
----------------
This line should be the first of four lines in the output
And this should be the second
# This should not appear (leading spaces but a comment)
This should be the third line of output
And this should be the last.
'''
