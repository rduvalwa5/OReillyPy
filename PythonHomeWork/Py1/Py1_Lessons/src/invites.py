'''
Created on Aug 3, 2012

@author: rduvalwa2
'''
#!/usr/local/bin/python3
"""invite.py demonstrates how to combine looping into a program """
invites = {} # empty dict
options = ['add','list','approve', 'delete', 'quit']
prompt = 'Pick an option from the list (%s): '%', '.join(options) # define a string that uses string join 
status_1 = 'un_approved'
status_2 = 'approved'
while True:  # simple way to create the while loop
  inp = input(prompt)  # saves on typing
  if inp not in options: # by making prompt and option variables save on typing
      print('Please select a valid option')
      continue # do not have to retype prompt
  if inp == 'add':
     name = input('Enter name:')
# case name
     if not name:
         continue
     invites[name] = status_1
# case list
  elif inp == 'list':
      for name, status in invites.items():
          print('%s (%s)' % (name, status))
# case approve
  elif inp == 'approve':
      for name in invites:
         if invites[name] == status_1:
             break
      else:
         print('There must be %s status invites.  Please pick another option' % status_1)
         continue
      while True:
         print('Please enter a valid name from the list below')
         unapproved = []
         for name in invites:
             if invites[name] == status_1:
                 unapproved.append(name)
         print(",".join(unapproved))
         name = input('Enter Name:')
         if not name:
               break # user changed mind about approving
         if name in unapproved:
             invites[name] = status_2
             print('%s %s' % (name,status_2))
             break
# case delete
# case delete
  elif inp == 'delete':
      if not invites:
          print('There must be invites before you delete any of them')
          continue # user changed mind about deleting             
      while True:
          print('Please enter a valid name from tne list below')
          for name, status in invites.items():
              print('%s (%s))' % (name, status))
          name = input('Enter name:')
          if not name:
               break
          if name in invites:
               del invites[name]
               print('%s deleted' % name)
               break
# case quit
  elif inp == 'quit':
      print('Quitting invites')
      print('The final invitation list follows')
      for name, status in invites.items():
             print('%s (%s)' % (name, status))
      break