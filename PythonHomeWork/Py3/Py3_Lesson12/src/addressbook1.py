'''
 addressbook1.py
'''
import shelve
import sys
from optparse import OptionParser

shelf_location = './email.shelf1'

def email_add(email):
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

def main(options):
    "routes request"
    if options.action == 'add':
        return email_add(options.email)
    elif options.action == 'delete':
        return email_delete(options.email)

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
    (options, args) = parser.parse_args()
    # validation
    if options.action is None:
        sys.exit("You must specify an action (add or delete) with '-a action'")
    if options.action and not options.email:
        parser.error("option -a requires option -e")
    elif options.email and not options.action:
        parser.error("option -e requires option -a")
    elif options.email and '@' not in options.email:
        parser.error("option -e requires a valid email address")
#    print(options)
    print(main(options)[1])      
         
