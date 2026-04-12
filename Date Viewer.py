"""
Converts a numeric date (year, month, day) into a readable format with
the correct month name and ordinal ending, such as 'April 21st, 2026'.
"""

# List of month names for conversion from integer
months = ["January", "Feburary", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# Generate a list of ordinal suffixes (st, nd, rd, th) for days 1-31
endings = ["st", "nd", "rd"] + 17 * ["th"] \
        + ["st", "nd", "rd"] + 7 * ["th"] \
        + ["st"]

# Prompt user for numeric date components
year = input("Year: ")
month = input("Month [1 to 12]: ")
day = input("Day [1 to 31]: ")

# Convert string inputs to integers for indexing
month_number = int(month)
day_number = int(day)

# Map the numeric input to the corresponding name and suffix
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

# Display the formatted date string
print(month_name + " " + ordinal + ", " + year)
