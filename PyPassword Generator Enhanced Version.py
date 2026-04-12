"""
Generates a randomized password using a user‑specified number of letters,
symbols, and numbers. The characters are selected randomly, combined,
shuffled, and returned as a final password.
"""
# Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Import required libraries
import random

total_characters = ""
total_symbols = ""
total_numbers = ""

for letter in range(nr_letters):
    total_characters += random.choice(letters)

for number in range(nr_numbers):
    total_numbers += random.choice(numbers)

for symbol in range(nr_symbols):
    total_symbols += random.choice(symbols)

# Combine everything into one string
combined = total_characters + total_symbols + total_numbers

# Turn the string into a list of characters
password_list = list(combined)

# Shuffle the list
random.shuffle(password_list)

# Build the final password
password = ""
for char in password_list:
    password += char

print("Your generated password is:", password)
