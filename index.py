# Python Crash Course

"""Learning Variables and Simple Data Types"""

# A Variable from my understanding is like a storage device or a folder that stores all kinds of things.
# Variable can be used to either store numbers, letters, names e.t.c
# Let's assume we have 3 types of medications: Panadol, Softgel and Cough Syrup
# we can assign a variable to each medication
# e.g medication1 = "Panadol"
# medication2 = "Softgel"
# medication3 = "Cough Syrup"
# or drugs = "Paradol, Softgel, Cough Syrup"

"""Combining Variables and Strings"""

# We can also combine variables together in another variable or combine a variable with a string
# e.g medications = medication1 + medication2 + medication3
# or medications = "'Eat your food before taking the' + medication1"

"""Classwork on Variables"""

# - Store Your Name: Create a variable that holds your name and print it in a sentence like: "Hello, my name is X."
my_name = 'John'
print("Hello, my name is " + my_name)

# - Age Calculator: Store your age in a variable, then calculate how old you’ll be in 10 years.
my_age = 20
print(my_age + 10)

# or
my_age = 20
years = 10
print("In 2035 I will be " + str(my_age + years) + " years old.")

# or
my_age = 20
years = 10
future_age = str(my_age + years)
print("Wow John would be " + future_age + " years old in 10 years")

# - Swap Values: Create two variables (e.g., a = 5, b = 10) and swap their values without reassigning directly.
a = 5
b = 10

# Using temporary variable to swap values
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)

# using tuple unpacking to swap values
x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)

# - String Length: Store a sentence in a variable and print how many characters it has using len().
sentence = "Learning Python is fun!"
print(len(sentence))
quote = "I would be successful in life"
print(len(quote))

# - Favorite Foods: Create a list of your favorite foods and print them in a sentence.
favorite_foods = ["rice", "beans", "plaintain"]
print("My favorite foods are: " + ", ".join(favorite_foods))


sentence = "I love Jesus"
print(len(sentence))

a = int(1)
b = int(2.5)
c = int("3")
cl = int(float("3.4"))
d = float(4)
e = float("2.5")
f = float("3")
g = float("4.23")
h = str("90s")
i = str(22)
j = str(3.01)
k = str("4.2")
l = round(int(float("3.5")))

print([a,b,c,cl,d,e,f,g,h,i,j,k,l])

print(type("Book"))
print(type(3))
print(type(3.5))
print(type(True))

total_score = 25
name = "John"

print("Dear Mr " + name + ",")
print("This is an email from the DSA of Covenant University")
print("This is to inform you that your total score for this semester is " + str(total_score) + " points in total of 30 points.")
print("Congratulations Mr Nwagboo, kindly print this email as your score sheet for the semester.")
print("Best Regards, \nDSA Covenant University.")

# try:
#     age = int(input("What's your age? "))
#     # Check if the user has exceeded the age limit for driving first
#     if age >= 70:
#         print("You have exceeded the age limit for driving")
#     # Then check if the user is eligible to drive (between 18 and 69)
#     elif age >= 18:
#         print("Congrats! you're eligible to drive.")
#     # Otherwise, the user is not eligible yet
#     else: 
#         print("You're not eligible to drive yet!")
# except ValueError:
#     print("Invalid input, please enter a real number!")


"""Exercise on Variables and Data Types"""

#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item_name = "Macbook Pro Laptop"
item_price = 500.00
in_stock = 50
print(item_name)
print(item_price)
print(in_stock)
is_in_stock = False
print(item_name, item_price, in_stock)
print("We have " + str(in_stock) + " pieces of " + item_name + " for $" + str(item_price) + " each.")

if is_in_stock:
	print(item_name + " is available in stock.")
else:
	print(item_name + " is currently out of stock.")






