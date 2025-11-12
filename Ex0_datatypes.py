# -------------------------------------------
# Exercise 0: Data Types Review
# -------------------------------------------
# In this exercise, we'll revise all the core Python data types covered so far:
# - Strings (str)
# - Integers (int)
# - Floats (float)
# - Booleans (bool)
# - Lists (list)
#
# Complete each task by writing code that solves the problem.
# Pay careful attention to data types!
# -------------------------------------------


# Task 1: Age Calculator
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Age Calculator\n"
    + "-------------------------------------------")
# Ask the user for their birth year (as an integer).
# Calculate their age by subtracting the birth year from 2025.
# Store the result in a variable called age.
# 
# Check if they are a Baby Boomer (born between 1946 and 1964).
# Store this True/False result in a variable called is_boomer.
# 
# Print both the age and whether they are a Baby Boomer.
#
# Example output:
# Your age: 65
# Are you a Baby Boomer? True
#
# Write your code below:
birth_yr=int(input("Enter your birth year: "))
current_age=2025-birth_yr
if 1946<=birth_yr<=1964:
    is_boomer=True
else:
    is_boomer=False
print(f"Your age : {current_age}")
print(f"Are you a Baby Boomer? {is_boomer}")




# Task 2: Price Calculator
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Price Calculator\n"
    + "-------------------------------------------")
# Create a list called prices with 3 prices: 5.99, 12.50, and 8.75
#
# Calculate the total price (sum of all three prices).
# Store it in a variable called total.
#
# Check if the total is more than 25.00.
# Store this True/False result in a variable called is_expensive.
#
# Print the total and whether it's expensive.
#
# Example output:
# Total: £27.24
# Is expensive (over £25): True
#
# Write your code below:
price_list=[5.99,12.50,8.75]
total=sum(price_list)
#if total>=25:
 #   is_expensive=true
#else:
 #   is_expensive= False
is_expensive =total>25
print(f"Total: {total:.2f}")
print("Is expensive (over 25) :",is_expensive)



# Task 3: Username Checker
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 3: Username Checker\n"
    + "-------------------------------------------")
# Ask the user to enter a username (string).
#
# Check if the username is valid. A valid username must be:
# - At least 5 characters long
# - Contains the letter "a" (lowercase)
#
# Store each check as a separate boolean variable:
# - is_long_enough
# - has_letter_a
#
# Print the username and both check results.
#
# Example output:
# Username: james
# Long enough (5+ chars): True
# Contains letter 'a': True
#
# Write your code below:
username=input("Enter a username: ")
if len(username)>=5:
    is_long_enough=True
else:
    is_long_enough=False
if "a" in username:
    has_letter_a =True
else:
    has_letter_a=False
print(f"Username : {username}")
print(f"Long enough (5+characters) :{is_long_enough}")
print(f"Contains letter 'a': {has_letter_a}")




# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've completed all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
