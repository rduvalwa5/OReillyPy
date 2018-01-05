import unittest
import addressbook1
   
class TestEmailHandlers(unittest.TestCase):
   
    def setUp(self):
        self.email = 'test123@t.com'
   
    def test_email_delete(self):
        addressbook1.email_add(self.email)  # ensure the email is active
        self.assertEqual(addressbook1.email_delete(self.email)[0], True)
        self.assertEqual(addressbook1.email_delete(self.email)[0], False)
           
    def test_email_add(self):
        self.assertEqual(addressbook1.email_add(self.email)[0], True)
        self.assertEqual(addressbook1.email_add(self.email)[0], False)

if __name__ == "__main__":
    unittest.main()

