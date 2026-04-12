"""
Simple password generator that creates a random password using letters,
symbols, and numbers chosen by the user.
"""

import random

# List of all possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Take user input for the quantity of each character type
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty string to build the password
password = ""

# Append random letters based on user count
for letter in range(nr_letters):
    password += random.choice(letters)

# Append random symbols based on user count
for symbol in range(nr_symbols):
    password += random.choice(symbols)

# Append random numbers based on user count
for number in range(nr_numbers):
    password += random.choice(numbers)

# Output the final generated password string
print("Your easy generated password is:", password) 
