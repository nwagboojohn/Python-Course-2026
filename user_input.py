# Code for testing user input

# name = input('What is your name?: ')
# print(f'Hi {name}')
# age = input('How old are you?: ')
# print('Wow, ' + name + ' you\'re ' + age + ' years old!')
# print(f'Hi {name}, how can GroocyAI help you today.')

# Simple Calculator

# num1 = input('Enter a digit: ')
# num2 = input('Enter another digit: ')
# answer = int(num1) + int(num2)
# print(f'{answer:.2f}')

# num1 = input('Enter a digit: ')
# num2 = input('Enter another digit: ')
# answer = float(num1) + float(num2)
# print(answer)


# Asking a user for few instructions and then storing them in appropriately

name = input('Enter your name: ')
age = int(input('Enter your age: '))
wage = int(input('How much is your hourly wage? '))
work_hour = int(input('How many hours do you work a day? '))
is_a_student = ''
while is_a_student != 'yes' and is_a_student != 'no':
   is_a_student = input('Are you a student (yes or no)? ').capitalize()
if is_a_student != 'yes' and is_a_student != 'no':
   print('Invalid input, please enter a digit number.')

print('====== Summary of your details ======')
print('Hi ' + name + ' here\'s your summary details')
print(f'You\'re {age} years old')
print(f'You earn ${wage} per hour and ${wage * work_hour * 7} per week cool!')
if is_a_student != 'no':
   print('Congrats!, you\'re a student')
else :
   print('You\'re not a student')


# Task 2
# Distance converter

# first_name = input('Enter first name: ')
# distance_km = float(input('Enter distance in km: '))
# distance_miles = float(round(distance_km / 1.609,1))
# print(f'Hello {first_name.title()}, you\'re {distance_km}km far from home and {distance_miles} miles away from home.')

# Addition and Subtraction

'''''num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
print(f'{num1} + {num2} = {num1 + num2}')
num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
print(f'{num1} * {num2} = {num1 * num2}')
num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
print(f'{num1} - {num2} = {num1 - num2}')'''''

