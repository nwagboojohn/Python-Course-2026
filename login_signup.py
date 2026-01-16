# a signup / login project

# signup, collects user details, name, email and password
print('--- Welcome to Python 101, kindly signup ---')
user_name = input('Enter username: ')
email = input('Enter email: ')
password = int(input('Enter password: '))

# login user details
while user_name:
    print('\n--- Login to continue your Python course ---')
    login_user = input('Enter username: ')
    login_password = int(input('Enter password: '))
    
    # matching user details

    if user_name == login_user and password == login_password:
        print(f'Congrats! signup was successful.')
    else :
        print('please enter correct email or password!')

print(f'Hello {user_name}, welcome to python 101')