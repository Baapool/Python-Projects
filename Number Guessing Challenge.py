"""
A simple number-guessing game where the player tries to guess a random
number between 1 and 100. The player starts with 100 points and loses
one point for every incorrect guess until they find the correct number.
"""

import random

# Initialize the starting score and generate a random target number
score = 100
random_number = random.randint(1, 100)

# Start the game loop
while True:
  # Take input from the user and convert to integer
  user_number_input = int(input('Guess : '))

  # Check if the guess matches the random number
  if user_number_input == random_number:
    print('Congratulations you won! Score: ' + str(score))
    break
  else:
    # Provide feedback and decrement score for incorrect guesses
    print('Better luck next time. Score: ' + str(score))
    score = score - 1