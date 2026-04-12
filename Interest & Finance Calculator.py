"""
A simple finance calculator that computes capital, interest rate,
interest amount, or time based on user input. Supports yearly interest
and optional month-based calculations.
"""
# Introduction
print("-----Interest, Interest Rate, Time and Capital Calculator-----")

# Ask what the user wants to calculate?
calculate_choice = input("What would you like to calculate (Capital, Interest Rate, Interest or Time): ").lower()

# Calculate Capital
if calculate_choice == "capital":
    interest_amount = float(input("How much is the yearly interest amount: "))
    interest_rate_percent = float(input("What is the interest rate in percent: "))
    if interest_rate_percent == 0:
        print("The interest rate cannot be zero when calculating capital.")
    else:
        capital = interest_amount / (interest_rate_percent / 100)
        print(f"The capital is {capital:.2f}")

# Calculate Interest Rate
elif calculate_choice == "interest rate":
    principal_amount_2 = float(input("How much is the capital: "))
    interest_amount_2 = float(input("How much is the yearly interest amount: "))
    if principal_amount_2 == 0:
        print("Capital cannot be zero when calculating the interest rate.")
    else:
        interest_rate = (interest_amount_2 / principal_amount_2) * 100
        print(f"The interest rate is {interest_rate:.2f}%")

# Calculate Interest
elif calculate_choice == "interest":
    principal_amount_3 = float(input("How much is the capital: "))
    interest_rate_percent_3 = float(input("What is the interest rate in percent: "))
    annual_interest_amount = principal_amount_3 * (interest_rate_percent_3 / 100)
    print(f"The yearly interest is {annual_interest_amount:.2f}")
