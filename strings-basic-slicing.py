msg = 'welcome to python 101: Strings'
print(msg)
print(msg,msg)
print(msg * 2)
print(msg + msg)
print(msg.upper())
print(msg.title())
print(msg.capitalize())
print(msg.lower() * 2)
print(len(msg)) # Counts how many letters including  are the 
print(msg.count('n')) # How many 'n' do are in the variable msg

# slicing string
print(msg[9]) # Reads letter at 9 starting from 0 
print(msg[0:7]) # The computer reads starting from 0 and stops at 6
print(msg[2:7]) # The computer reads starting from 2 and stops at 6
print(msg[1:9]) # The computer reads starting from 1 and stops at 8
print(msg[5:7])

'''Task'''
# From the string 'Welcome to Python 101: Strings', extract text and create / print a new string that says
# '1 Welcome Ring To Tyler'
msg_2 = msg[18] + ' ' + msg[:7] + ' ' + msg[25:29] + ' ' + msg[8:10] + ' ' + msg[8]+msg[12]+msg[2]+msg[1]+msg[25]
print(msg_2.title())

'''Task2'''
# Print the same string backwards...
# Hint: Google is your friend...
text = 'Google is your friend'
print(text[::-1])


# '''Custom Data Parser'''
# - Ask the user to enter a sentence.
# - Split it into words and store them in a list.
# - Print the number of words, the longest word, and whether any word is numeric.


# request users input for a sentence
user_input = input('Enter a sentence: ')

# split users sentence to words
splited_words = user_input.split()

# gets the number of words from users sentence
number_of_words = len(splited_words)

if True:
    # get longest word from users sentence
    longest_word = max(splited_words, key=len)

    # check if any splited word is numeric
    numeric_word = any(word.isdigit() for word in splited_words)

    # print all summary statements
    print('\n---- Summary of details ----')
    print('Number of words :', number_of_words)
    print('Longest word :', longest_word)
    print('Any numeric word :', numeric_word)




