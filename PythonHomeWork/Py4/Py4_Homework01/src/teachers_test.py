'''
I'd like to see these two test verbaitm in your next draft, i.e. don't 
add print( ) -- printing from tests is considered poor form -- and do
not change the API to accept a 2nd argument to Composable.
Leave these exactly as they are.  Thanks in advance.
'''

def test_inverse(self):
reverser = Composable(reverse)
nulltran = reverser ** 2  #  reverser -- commenting out what was a mulitplicand
    for s in "", "a", "0123456789", "abcdefghijklmnopqrstuvwxyz":
        self.assertEquals(nulltran(s), s)
    
def test_square(self):
        squarer = Composable(square)
        po4 = squarer ** 2  #  square
        for v, r in ((1, 1), (2, 16), (3, 81)):
            self.assertEqual(po4(v), r)
