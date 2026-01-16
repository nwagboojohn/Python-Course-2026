# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

"""Arcade Day Pass TRacker"""

# Variables to store customer and pass details
customer_name = "Alice John"
no_of_passes = 5
tokens_per_pass = 10
price_per_pass = 15.00
tokens_required_per_game = 5
 
# Calculation of total tokens, cost and games available
total_tokens = tokens_per_pass * no_of_passes

total_cost = price_per_pass * no_of_passes 

games_available = total_tokens // tokens_required_per_game

# Print summary:
print("Hi " + customer_name + ", Here's a summary of your \nArcade Day Pass Tracker")
print('Customer Name :', customer_name)
print('No of passes :', no_of_passes)
print('Total tokens :', total_tokens)
print('Total cost :' + str(total_cost))
print(f'Total cost : ${total_cost:.2f}')
print('Games available : ' + str(games_available))


