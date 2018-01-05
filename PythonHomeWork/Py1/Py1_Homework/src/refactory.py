#!/usr/local/bin/python3
"""Building and debugging Objective 1: refactory.py"""

small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
        """ Takes a string and returns a book title style string.
        All words EXCEPT for small words are made title case
        unless the string starts with a preposition, in which
        case the word is correctly captalized.

        >>> book_title('DIVE Into python')
        'Dive into Python'

        >>> book_title('the great gatsby')
        'The Great Gatsby'

        >>> book_title('the WORKS OF AleXANDer dumas')
        'The Works of Alexander Dumas'
        """
        # this will capitalize the first letter of every word
        title = title.title()
        pre_title = []
        pre_title = title.split(" ")
        new_title = ""
        for word in pre_title:
                # If the word is the first word of the title it has to be capitalize
                if word != pre_title[0]:
                # If the word is in the small word list make it lower case
                        if word.lower() in small_words:
                                word = word.lower()
                new_title = new_title + word + ' '
# Remove the lagging space                      
        return new_title.strip()

def _test():
        import doctest, refactory
        return doctest.testmod(refactory)

if __name__ == "__main__":
 _test()
