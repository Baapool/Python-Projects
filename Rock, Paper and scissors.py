"""
A simple Rock-Paper-Scissors game where the player chooses an option,
the computer randomly selects one, and the program determines the winner.
Includes a loop to allow playing multiple rounds.
"""

import random

# Function to handle user input and computer's random choice
def get_choices():
    player_choice = input("Enter a choice [Rock, Paper, Scissors]: ").lower().strip()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    options_menu = {"player": player_choice, "Computer": computer_choice}
    return options_menu

# Function to compare choices and determine the winner
def check_winner(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    # TIE
    if player == computer:
        return "It's a tie!"
    # Player Wins
    elif player == "rock" and computer == "scissors":
        return "Rock smashes Scissors! You won!"
    # Player Wins
    elif player == "paper" and computer == "rock":
        return "Paper covers Rock! You won!"
    # Player Wins
    elif player == "scissors" and computer == "paper":
        return "Scissors cuts Paper! You won!"
    # Player loses
    elif player == "paper" and computer == "scissors":
        return "Scissors cuts Paper, You lose."
    # Player loses
    elif player == "rock" and computer == "paper":
        return "Paper covers Rock, You lose."
    # Player loses
    else:
        return "Rock smashes Scissors, You lose."



# Main game loop to allow multiple rounds.
while True:
    # Get choices from the user and computer
    choices = get_choices()
    # Determine the result of the round
    result = check_winner(choices["player"], choices["Computer"])
    print(result)

    # Ask if the player wants to continue
    play_again = input("Do you want to play another round? [yes/no]: ").lower().strip()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
