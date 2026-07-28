# Import required Libraries.
import random

# Print out the logo and the welcome screen.
logo = r"""
  _   _                 _                  _____                     _                _____ _           _ _                       
 | \ | |               | |                / ____|                   (_)              / ____| |         | | |                      
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |    | |__   __ _| | | ___ _ __   __ _  ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | |    | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |____| | | | (_| | | |  __/ | | | (_| |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|
                                                                              __/ |                                     __/ |     
                                                                             |___/                                     |___/      
"""
print(logo)
print("🤔 I am thinking of a number between 1 and 100.\n")


# Number to guess
number = random.randint(1, 100)

# Ask the user to choose the difficulty.
difficulty = input("Choose a difficulty level. Type 'Easy' or 'Hard': ").lower().strip()

match difficulty:
    case "easy":
        attempts = 10
    case "hard":
        attempts = 5
    case _:
        attempts = 10
        print("Invalid choice. Defaulting it to Easy.")





while attempts > 0:

    if attempts == 1:
        print(f"\nYou have {attempts} attempt remaining.")
    else:
        print(f"\nYou have {attempts} attempts remaining.")


    guess = int(input("Make a guess: "))

    if not 1 <= guess <= 100:
        print("Please enter a number between 1 and 100.")
        continue


    if guess == number:
        print(f"\n🎉 You got it! The number was {number}.")
        break

    attempts -= 1

    if guess > number:
        print("Too high.")
    else:
        print("Too low.")

    if attempts > 0:
        print("Guess again!")

else:
    print(f"\n💀 You've run out of guesses. The number was {number}.")