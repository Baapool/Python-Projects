"""
PyMiniTools is a menu-based collection of simple Python practice programs, including
math operations, conversions, name formatting, and other beginner-friendly tools.
"""

# Function to greet the user by name
def greeting_name():
  name = input("What is your name? Write here: ")
  print("Hello, " + name)

# Function for basic math operations (Addition, Subtraction, Multiplication, Division)
def simple_arithmetic():
  try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    operation = input("What would you like to do? Addition, Subtraction, Multiplication and Division: ").title()

    if operation == "Addition":
      print(f"{num1} plus {num2} is equals to {num1 + num2}.")
    elif operation == "Subtraction":
      print(f"{num1} minus {num2} is equals to {num1 - num2}.")
    elif operation == "Multiplication":
      print(f"{num1} multiplied by {num2} is equals to {num1 * num2}.")
    elif operation == "Division":
      if num2 != 0:
        print(f"{num1} divided by {num2} is equals to {num1 // num2}.")
      else:
        print("Error: Cannot divide by zero.")
    else:
      print("Sorry, I did not recognize that operation.")
  except ValueError:
    print("Invalid input. Please enter numeric values.")

# Function to determine if a number is Odd or Even
def odd_or_even():
  try:
    num = int(input("Your number: "))
    if num % 2 == 0:
      print("Even")
    else:
      print("Odd")
  except ValueError:
    print("Please enter a valid integer.")

# Function to calculate the area of a circle given its radius
def area_of_a_circle():
  try:
    radius = float(input("Radius of your Circle: "))
    # Using 3.14 as a simple approximation of Pi
    print(f"Area of your Circle is {3.14 * radius * radius}")
  except ValueError:
    print("Please enter a valid number for the radius.")

# Function to convert Celsius to Fahrenheit
def temperature_conversation():
  try:
    celsius = float(input("Write your Temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Your temperature is {fahrenheit}°F")
  except ValueError:
    print("Please enter a valid temperature value.")

# Function to find the largest of three numbers
def maximum_of_three_numbers():
  try:
    n1 = int(input("Your First number: "))
    n2 = int(input("Your second number: "))
    n3 = int(input("Your third number: "))
    greatest = max(n1, n2, n3)
    print(f"{greatest} is the greatest.")
  except ValueError:
    print("Please enter valid integers.")

# Function for simple interest calculation
def simple_interest_calculator():
  try:
    p = float(input("Enter your Principal Amount: "))
    r = float(input("Enter your Rate of Interest (in %): "))
    t = float(input("Enter your Time (in years): "))
    interest = (p * r * t) / 100
    print(f"Your interest is {interest}.")
  except ValueError:
    print("Invalid input. Please enter numbers.")

# Function to print the multiplication table of a number
def multiplication_table():
  try:
    number = int(input("Write your number here: "))
    for i in range(1, 11):
      print(f"{number} x {i} = {number * i}")
  except ValueError:
    print("Please enter a valid integer.")

# Repeated function: Keeping original structure but adding comments
def even_and_odd_number_teller():
  odd_or_even()

# Function to format and capitalize names
def capitalize_name():
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    print(f"Hi there, {f_name.title()} {l_name.title()}!")

# Main menu dictionary to map choices to functions
functions_menu = {
    "1": {"name": "Greeting Name", "func": greeting_name},
    "2": {"name": "Simple Arithmetic", "func": simple_arithmetic},
    "3": {"name": "Odd or Even", "func": odd_or_even},
    "4": {"name": "Area of a Circle", "func": area_of_a_circle},
    "5": {"name": "Temperature Conversion", "func": temperature_conversation},
    "6": {"name": "Maximum of Three Numbers", "func": maximum_of_three_numbers},
    "7": {"name": "Simple Interest Calculator", "func": simple_interest_calculator},
    "8": {"name": "Multiplication Table", "func": multiplication_table},
    "9": {"name": "Even and Odd Number Teller", "func": even_and_odd_number_teller},
    "10": {"name": "Capitalize First letter of your names", "func": capitalize_name}
}

# Main Loop to keep the program running until the user exits
while True:
    print("\n----- Python Practice Programs Menu -----")
    for key, value in functions_menu.items():
        print(f"{key}. {value['name']}")
    print("11. Exit")
    print("-----------------------------------------")

    choice = input("Enter your choice (1-11): ")

    if choice == '11':
        print("Exiting the program. Goodbye!")
        break
    elif choice in functions_menu:
        print(f"\nExecuting: {functions_menu[choice]['name']}")
        try:
            functions_menu[choice]['func']()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")