"""
Converts a numeric date (year, month, day) into a readable format with
the correct month name and ordinal ending, such as 'April 21st, 2026'.
"""

logo = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣤⠀⠿⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⠿⠀⣤⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠒⠒⠒⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠒⠒⠒⠛⠛⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⡟⢻⣿⣿⡟⣿⣿⣿⠛⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣛⣛⠛⣛⣛⡋⠈⣛⣛⡃⢘⣛⣛⠁⢙⣛⣛⠀⣛⣛⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⡇⢸⣿⣿⡇⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣉⣉⠀⣉⣉⣉⢈⣉⣉⡁⢈⠉⠉⡁⣉⣉⣉⠀⣉⣉⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⡇⠀⠰⠂⠀⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣭⣭⠀⣭⣭⣅⢀⣭⣭⡅⢨⣤⣤⡀⣨⣭⣭⠀⣭⣭⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⠀⣿⣿⣿⢸⣿⣿⡇⢸⣿⣿⡇⣿⣿⣿⠀⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣤⣤⠀⣤⣤⣤⢠⣤⣤⡄⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣤⣿⣿⣿⣼⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
"""

# List of month names for conversion from integer
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

# Generate a list of ordinal suffixes (st, nd, rd, th) for days 1-31
endings = ["st", "nd", "rd"] + 17 * ["th"] \
        + ["st", "nd", "rd"] + 7 * ["th"] \
        + ["st"]

# Prompt user for date components
year = input("Year: ")
while not year.isdigit() or len(year) > 4:
    year = input("Year: ")

month = input("Month [January to December]: ")
while month not in months:
    month = input("Month [January to December]: ")

day = input("Day [1 to 31]: ")
while day not in days:
    day = input("Day [1 to 31]: ")

# Convert day to an integer for indexing
day_number = int(day)

# Get the ordinal suffix for the day
ordinal = day + endings[day_number - 1]

# Display the formatted date string
print("\n" * 20)
print(logo)
print(month + " " + ordinal + ", " + year)