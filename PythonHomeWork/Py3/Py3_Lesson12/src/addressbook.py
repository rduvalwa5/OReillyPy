import configparser
from optparse import OptionParser
import shelve
# import sys

# Remove to add configparser
shelf_location = './email.shelf'
# config = configparser.RawConfigParser()
# config.read('/Users/rduvalwa2/DevTools/eclipse-indigo/workspace/Python3_Git/Py3_Git/email.shelf')
# shelf_location = config.get('database','file)')



class InvalidEmail(Exception):
    pass

def validate_email(email):
    if '@' not in email:
        raise InvalidEmail("Invalid email: " + email)

def email_add(email):
    validate_email(email)
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    emails = shelf['emails']
    if email in emails:
        message = False, 'Email "%s" already in address book' % email
    else:
        emails.append(email)   
        message = True, 'Email "%s" added to address book' % email       
    shelf['emails'] = emails
    shelf.close()
    return message

def email_delete(email):
    validate_email(email)
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    emails = shelf['emails']
    try:
        emails.remove(email)
        message = True, 'Email "%s" removed from address book' % email
    except ValueError:
        message = False, 'Email "%s" was not in the address book' % email       
    shelf['emails'] = emails           
    shelf.close()
    return message

def email_display():
    shelf = shelve.open(shelf_location)
    emails = shelf['emails']
    shelf.close()
    text = ''
    for email in emails:
        text += email + '\n'
    return True, text

def main(options):
    "routes requests"
    if options.action == 'add':
        return email_add(options.email)
    elif options.action == 'delete':
        return email_delete(options.email)
    elif options.display == True:
        return email_display()
    
if __name__ == '__main__':
    shelf = shelve.open(shelf_location)
    if 'emails' not in shelf:
        shelf['emails'] = []
    shelf.close()
    parser = OptionParser()
    parser.add_option('-a', '--action', dest="action", action="store",
                            help="requires -e option. Actions: add/delete")
    parser.add_option('-e', '--email', dest="email",
                            action="store", help="email used in the -a option")
    # OTPPASER Type validation optparse module also includes type checking for string, float, and choices
    parser.add_option('-d', '--display', dest="display", type="int", action="store", help="show all emails limited by value")    
#    parser.add_option('-d', '--display', dest="display", action="store_true",help="show all emails")    
    (options, args) = parser.parse_args()
    # validation
#    if options.action is None:
#        sys.exit("You must specify an action (add or delete) with '-a action'")
    if options.action and not options.email:
        parser.error("option -a requires option -e")
    elif options.email and not options.action:
        parser.error("option -e requires option -a")
    try:  
        print(main(options)[1])
    except InvalidEmail:
        parser.error("option -e requires a valid email address")
