"""
A simple blind auction program where each bidder enters their name and bid
privately. All bids are stored, and the program determines and displays
the highest bidder at the end.
"""

#Print out the logo.
logo = r'''
                       -----------
                       \         /
                        )_______(
                        |"""""""|_.-._,.---------.,_.-._
                        |       | | |               | | ''-.
                        |       |_| |_             _| |_..-'
                        |_______| '-' `'---------'` '-'
                        )"""""""(
                       /_________\\
                     .-------------.
                    /_______________\\
'''
print(logo)

# Ask for name input
name = input("What is your name: ")
bid = int(input("What is your bid: $"))

# Add Name and bid into the dictionary as the key and value.
names_and_bids = {name: bid}

# Ask if there are other users who want to bid.
game = 0
while game == 0:
    ask_again = input("Is there anyone else to bid? [Yes or No]: ")
    if ask_again.upper() == "YES":
        print("\n" * 100)
        name = input("What is your name: ")
        bid = int(input("What is your bid: $"))
        names_and_bids[name] = bid
    else:
        game = 1

# Find the highest bid in the dictionary.
highest_bid = 0
winner = ""

for bidder in names_and_bids:
    amount = names_and_bids[bidder]
    if amount > highest_bid:
        highest_bid = amount
        winner = bidder

print(f"SOLD to bidder {winner} for ${highest_bid}.")
