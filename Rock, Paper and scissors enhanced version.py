"""
A simple Rock-Paper-Scissors game where the player chooses an option,
the computer randomly selects one, and the program determines the winner.
Includes a loop to allow playing multiple rounds.
"""

import random

# Function to handle user input and computer's random choice
def get_choices():
  player_choice = input("Enter a choice [Rock, Paper, Scissors]: ")
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "Computer": computer_choice}
  return choices

# Function to compare choices and determine the winner
def check_win(player, Computer):
  print(f"You chose {player}, Computer chose {Computer}")
  if player == Computer:
    return "It's a tie!"
  elif player == "Rock":
    if Computer == "Scissors":
      return "Rock smashes Scissors! You won!"
    else:
      return "Paper covers Rock! You lose."
  elif player == "Paper":
    if Computer == "Rock":
      return "Paper covers Rock! You won!"
    else:
      return "Scissors cuts Paper! You lose."
  elif player == "Scissors":
    if Computer == "Paper":
      return "Scissors cuts Paper! You won!"
    else:
      return "Rock smashes Scissors! You lose."

# Main game loop to allow multiple rounds
while True:
    # Get choices from user and computer
    choices = get_choices()
    # Determine the result of the round
    result = check_win(choices["player"], choices["Computer"])
    print(result)

    # Ask if the player wants to continue
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
