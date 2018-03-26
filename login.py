import os

''' program logs in staff members only through usernames and password '''

print("To login please enter your user name below.")

# Take input from the user
user = input("Enter name:::::::::")

if user == 'admin':
    print(user,"Welcome Admin kindly login")
    password = input("Enter Password:::::::::")
    if password == 'ray':
        print ('you have succefully logged in')
    else:
        print ('Sorry access denied', user)
        
elif user == 'secretary':
    print(user,"Welcome secretary kindly login")
    password = input("Enter Password:::::::::")
    if password == 'carol':
        print ('you have succefully logged in')
    else:
        print ('Sorry access denied')
        
elif user == 'manager':
    print(user,"Welcome manager kindly login")
    password = input("Enter Password:::::::::")
    if password == 'russell':
        print('you have successfully logged in')
    else:
        print('Sorry access denied')
        
elif user == 'accountant':
    print(user,"Welcome accountant kindly login")
    password = input("Enter Password:::::::::")
    if password == 'trevor':
        print('you have successfully logged in')
    else:
        print('Sorry access denied')
        
elif user == 'members':
    print(user,"Welcome members kindly login")
    password = input("Enter Password:::::::::")
    if password == 'partner':
        print('you have successfully logged in')
    else:
        print('Sorry access denied')

else:
    print("Invalid username!")
        
        
    
        

