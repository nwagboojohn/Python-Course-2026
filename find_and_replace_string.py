# # find and replace strings in  variables
# msg = 'Welcome to Python 101: Strings'
# print(msg.replace('Welcome', 'Welcome!')) # The first string is the value to be replaced, the second string the replaced value.
# print(msg.find('Python'))
# print(msg.find('null')) # If the system cannot find the inputed string, it prints -1 as the result -- Note that Python programming is case sensitive

# # membership in python
# member = 'Welcome to Python 404 : Community'
# print('Python' in member) # Checks if the value in string exist, if yes it prints True, if not it prints False.
# print('404' not in member) # Checks if the value in string does not exist, if yes it prints True, if not it prints False.

# # Task
# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# username = input('\nEnter username: ')
# email = input('Enter email: ')
# age = int(input('Enter your age: '))
# is_a_student = input('Are you a student (Yes or No)? ').capitalize()
# type_of_company = input('What type of company would you like to build (AI or Manual)? ').upper()
# company_worth = int(input('How much revenue would you like your company to generate in dollars? '))

# print('\n===== Summary of Details =====')

# if is_a_student != 'Yes' :
#     print(f'Hi {username}, as a {age} year old graduate building a/an {type_of_company} company worth ${company_worth}M, you must possess the spirit of entrepreneurship!')   
# else :
#     print(f'Nice question {username}, as a {age} year old ambitious student, building a/an {type_of_company} company worth ${company_worth}M means you must have a mindset different from other students!')


text = 'I love python 101 programming a lot and I\'m willing to commit to learning it in order to build AI Agents and help the society and world at large.'
extract_text = f'{text[0]} {text[2:6]} {text[7:13]} {text[95:97]} projects e.g admin dashboard that helps a vendor regulate sales without much hussle.'
replace_text = text.__add__('building')
print('\n===== Results Summary ====')
print(f'{extract_text} \n{replace_text}')
