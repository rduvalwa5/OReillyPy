"""Compare my title function to str.title()"""
import unittest

def title(s):
    "How closes is this function to str.title()"""
    the_return = []
    for word in s.split():
        new_word = ''
        for ch in word:
            if ch[0]:
                new_word + ch.upper()
            else:
                new_word + ch.lowere()
        the_return.append(word.title())
    return ' '.join(the_return)
    
class TestTitle(unittest.TestCase):
    def test_good_match(self):
        str = 'moby dick And Captian Ahab'
        message = title(str) + " does not match " + str.title()
        self.assertEqual(title(str), str.title(), message)

    def test_single_letter_match(self):
        str = 'a'
        message = title(str) + " does not match " + str.title()
        self.assertEqual(title(str), str.title(), message)

    def test_apostophe_match(self):
        str = 'Don\'t look now'
        message = title(str) + " does not match " + str.title()
        self.assertEqual(title(str), str.title(), message)
            
    def test_not_lower_match(self):
        str = 'What gooD IS aLL thIs EFFORT.'
        message = title(str) + "  matched lower " + str.lower()
        self.assertNotEqual(title(str), str.lower(), message)

    """ force failure for example look
    def test_not_upper_match(self):
        str = 'What gooD IS aLL thIs EFFORT?'
        message = title(str) + "  matched upper " + str.upper()
        self.assertEqual(title(str), str.upper(), message)
    """
if __name__ == "__main__":
    unittest.main()    