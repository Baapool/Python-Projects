"""
Rock, Paper and Scissors game using ASCII art. The player selects 0 for
rock, 1 for papper and 2 for scissors. The computer randomly chooses,
and the program displays the artwork and determines the winner.
"""

# ASCII Art for the game choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# List to store the ASCII art for easy indexing
list_of_choices = [rock, paper, scissors]

# Main game loop to allow multiple rounds
while True:
    # Ask the user for an input and convert to integer
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for Scissors.\n"))

    # Validate user input and display their choice
    if 0 <= user_choice <= 2:
        print("You chose:")
        print(list_of_choices[user_choice])

        # Computer makes a random choice between 0 and 2
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(list_of_choices[computer_choice])

        # Game Logic: Checking who won the round
        # Winning conditions for the user
        if user_choice == 1 and computer_choice == 0:
            print("Paper beats Rock, You win!")
        elif user_choice == 0 and computer_choice == 2:
            print("Rock beats Scissors, You win!")
        elif user_choice == 2 and computer_choice == 1:
            print("Scissors beats Paper, You win!")

        # Losing conditions for the user
        elif user_choice == 2 and computer_choice == 0:
            print("Rock beats Scissors, You lose.")
        elif user_choice == 1 and computer_choice == 2:
            print("Scissors beats Paper, You lose.")
        elif user_choice == 0 and computer_choice == 1:
            print("Paper beats Rock, You lose.")

        # Draw conditions
        else:
            print("It's a draw.")
    else:
        print("Invalid choice. Please try again with 0, 1, or 2.")

    # Ask if the player wants to continue
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing the enhanced version!")
        break