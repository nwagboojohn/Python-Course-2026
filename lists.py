# # Tutorial on List
# # todo: Check & write the difference between len() and count() functions
# groceries = ['Fish', 'Bread', 'Meat', 'Egg']
# numbers = [4, 5, 1, 2, 3]
# print(numbers)
# numbers.reverse() #* prints backwards
# print(numbers)
# numbers.sort() #* prints in accending order 
# print(numbers)
# numbers.sort(reverse=True) #* prints in decending order
# print(numbers)

# # todo: Check the maximum and minimum numbers in a digit list and also sum them
# print(min(groceries))
# print(max(groceries))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# # todo: modifing a list by extending, inserting and appending new items into a list
# groceries.append('Vegetables')
# print(groceries)
# groceries.insert(1, 'Tomatoes')
# print(groceries)
# groceries[0]= 'Mango' #* This is how to replace an item in a list 
# print(groceries) #* Note: that a list does not support the .replace() function like a variable would.
# #! groceries.replace('Mango', 'Apple') <== A list does not support this.
# '''Extending / Combining to list to form a single list.'''
# groceries.extend(numbers)
# print(groceries) # extend modifies groceries list in place by adding two list together.
# groceries.remove('Meat')
# print(groceries)
# groceries.pop(1) # Removes the second item in the list to be reused later
# print(groceries)
# groceries.pop() # By default removes the last item in the list but can be reused
# print(groceries)
# # clears all item in list 
# # ?groceries.clear()
# # ?print(groceries)
# #! Deletes all item in list
# del groceries[3]
# print(groceries)

# # todo: 4 different ways to copy a list 
# new_groceries = groceries
# print(new_groceries)
# new_groceries = groceries[:]
# print(new_groceries)
# new_groceries = groceries.copy()
# print(new_groceries)
# new_groceries = list(groceries)
# print(new_groceries)

# import copy # allows the copy. function to work properly
# groceries = ['Fish', 'Bread', ['Salt']]

# a = groceries               # alias
# b = groceries[:]            # shallow copy
# c = groceries.copy()        # shallow copy
# d = list(groceries)         # shallow copy

# print(a is groceries)  # True
# print(b is groceries)  # False

# a.append('Meat')        # affects groceries
# b.append('Egg')         # does not affect groceries

# groceries[2].append('Pepper')  # nested mutation visible in all shallow copies

# e = copy.deepcopy(groceries)   # deep copy
# groceries[2].append('Sugar')   # e unaffected
# print(groceries, b, c, d, e)

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [3, 4, 5, 1, 2, 7, 0, 50]
print(friends)
friends.append('TerryG') # saves or adds an item at the extreme end of the list
print(friends)
friends.insert(1, 'TerryG') # adds item in specified direction
print(friends)
friends[0] = 'Look' # eliminates an item in a position and replaces it with another item
print(friends)
friends.remove('Terry') # removes an item from the list
print(friends) #? Note: that removes takes only one argument i.e You can not remove more than one item with the .remove() function
friends.pop(3) # Does something similar to the .remove() function but actually different from it, while the .remove() function forgets an item, the .pop() function removes the item allowing users to access the removed item whenever.
print(friends)
# friends.clear() # Emptys the whole list
# print(friends)
del friends[0:2] # deletes the whole list or parts of the list
print(friends) #! This prints an error because a deleted list can't be printed
# friends.extend(cars) # combines, extends or joins two lists together.
# print(friends)
#todo: List copying
friends = friends[:] # shallow copying
print(friends)
friends.copy() # shallow copying
print(friends)

git remote add origin https://github.com/Nemejohn/Python-Course-2026.git
git branch -M main
git push -u origin main









