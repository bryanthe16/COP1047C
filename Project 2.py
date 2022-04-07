# Needed for the math.ceil function
import math

# Assumed number of items in each package
num_of_hotdogs_in_package = 10
num_of_buns_in_package = 8

# This will make the user input the data required
num_of_people = int(input("How many people are coming: "))
num_of_hotdogs_per_person = int(input("How many hot dogs per person: "))

# This is the main calculation
total_hotdogs = num_of_people * num_of_hotdogs_per_person

# Calculation for needed items
hotdogs_needed = total_hotdogs / num_of_hotdogs_in_package
buns_needed = total_hotdogs / num_of_buns_in_package

# Calculation for leftovers
hotdogs_leftover = total_hotdogs % num_of_hotdogs_in_package
buns_leftover = total_hotdogs % num_of_buns_in_package

# Print statements
# math.ceil is needed as it always comes out as a decimal and needs to round up
print(f'The minimum number of packages of hot dogs required:', math.ceil(hotdogs_needed))

print(f"The minimum number of packages of hot dog buns required:", math.ceil(buns_needed))

print("The number of hot dogs that will be left over:", hotdogs_leftover)

print("The number of hot dog buns that will be left over:", buns_leftover)