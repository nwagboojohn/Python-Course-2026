# # todo The Capstone – "The Grocery Budgeter"
# ? The Task: Create a program that helps a user calculate the cost of their groceries and tracks what they bought.
# grocery_list = []
# budget = 100.0  #? set budget to $100
# user_grocery_item = ''
# while user_grocery_item != 'checkout':
#     user_grocery_item = input('Enter grocery item or enter \"checkout\" to purchase: ')
#     user_grocery_price = float(input('Enter item price: '))
#     user_grocery_quantity = int(input('Enter item quantity: '))
    
#     #* exit condition when "exit" is entered
#     if user_grocery_item == 'checkout':
#         break
    
#     #* add or save item details in gorcery list
#     grocery_list.append(user_grocery_item)
    
#     #* calculate buyers total cost
#     total_cost = user_grocery_price * user_grocery_quantity
#     remaining_budget = budget - total_cost
    
# #? print item details and remaining budget
# print('\n====== Summary of Purchase ======')
# print(f'\nYou bought: [{grocery_list[-1]}] for ${total_cost:.2f}')
# print(f'Remaining budget: ${remaining_budget:.2f}')
    

# grocery_list = []
# budget = 100.0 # customer's budget
# # requests buyer's item
# buyer_item = input('Enter an item: ')
# # save buyer's item in grocery list
# grocery_list.append(buyer_item)
# # requests item details from buyer
# item_price = float(input('Enter item price: '))
# item_quantity = int(input('Enter item quantity: '))

# # calculate cost of purchase
# total_cost = item_price * item_quantity
# budget_variance = budget - total_cost
# positive_budget_variance = abs(budget_variance)

# # print purchase summary
# print('\n==== Purchase Summary ====')
# print(f'You bought: {grocery_list}')
# print(f'Total cost: ${total_cost}')
# print(f'Remaining budget: ${budget_variance}')
# # tell buyer whether or not total coat is less than budget
# if total_cost > budget:
#     print(f'You owe ${positive_budget_variance}')


# # todo The "Mad Libs" Generator
# ? The Task: Create a program that asks the user for specific words and then plugs them into a funny story.
# # variables that store user part of speech
# noun = []
# verb = []
# adjective = []
# # requests user inputs
# user_noun = input('Enter a noun, e.g Dog: ')
# user_verb = input('Enter a verb, e.g Cooked: ')
# user_adj = input('Enter an adjective, e.g Beautiful: ')
# # saves user\'s inputs in specified variables
# noun.append(user_noun)
# verb.append(user_verb)
# adjective.append(user_adj) 
# # collects users inputs to form a sentence
# print(f'The {user_adj} {user_noun}, likes to {user_verb} everyday.')

# # todo The "Tip Calculator"
# ? The Task: Write a program that calculates how much to tip a waiter.
# username = input('Enter username: ')
# bill = float(input('What\'s your total bill amount in decimal: '))
# tip_percentage = int(input('Enter tip percentage: '))
# tip_amount = bill * (tip_percentage / 100)
# tip_amount = round(tip_amount, 2)
# total = bill + tip_amount
# # prints user summary details
# print('\n==== Prints Tip Summary ====')
# print(f'Hi {username}, it feels good to show love \nYour Calculated Tip : ${tip_amount} \nYour Final Total : ${total:.2f}')

# todo The "RPG Inventory" System
# ? The Task: You are building a simple inventory for a Role-Playing Game (RPG)
# A list that contains loots the Game player got from his fight
inventory = ['Sword', 'Shield', 'Potion']
# prints the first item or loot in the list
print(f'First item : {inventory[0]}')
# requests new loot from gamer
loot_type = input('What loot did you just find? ')
# saves user's loot type and adds it to the end of the inventory list
inventory.append(loot_type)
# prints the last item in the list
print(f'Last item: {inventory[-1]}') # * using [-1] gets the last item in the list
# prints the full inventory list to show update
print('\n==== Summary of Loots ====')
print(f'Hi gamer, you updated your loot list')
print(f'Last item : {loot_type}') 
print(f'Last item position: {inventory.index(loot_type)}')
print(f'Full inventory: {inventory}')


