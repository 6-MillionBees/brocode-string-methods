# Arden Boettcher
# 9/18/24
# Verification Practice

username = input('Please enter your username: ')

while True: # I use while loops a lot
    if len(username) > 24:
        print('Character limit is 24')
        input('Please re-enter your username: ')
    elif username.isspace() == True:
        print('You have to put in an actual username (it can\'t just be spaces)')
        input('Please re-enter your username: ')
    elif username.isalnum() == False:
        print('No special characters')
        input('Please re-enter your username: ')
    elif username.isidentifier() == False:
        print('Username must not start with a number')
        input('Please re-enter your username: ')
    else:
        print('Welcome to {website}')
        break