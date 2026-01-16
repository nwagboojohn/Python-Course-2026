# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

print('\n==== Welcome to Pit Stop Timing Optimizer ====')
total_race_sec = float(input('Enter total race in seconds: '))
num_of_pit = int(input('How many pit stops were made? '))
avg_pit_stop = float(input('Enter average pit stop duration in seconds: '))

total_pit_stop_time = avg_pit_stop * num_of_pit
per_race_spent_in_pit = ((total_pit_stop_time / total_race_sec) * 100) if total_race_sec > 0 else 0
rounded_per = round(per_race_spent_in_pit, 2)

print('\n==== Summary of details ====') 
print(f'Total pit stop time (in seconds): {total_pit_stop_time} secs')
print(f'Percentage of race time spent in pits: {rounded_per}%')
# A function to check if pit time is > than 5% of the race
if rounded_per > 5:
    print('You need a new pit crew. 🛠️')

