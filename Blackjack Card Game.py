# Import the required Libraries
import random

# Print out the logo
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Asks the User to make
game = input("Do you want to play a game of BlackJack? (Yes or No): ").strip().lower()

playing = True

# Cards deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def display_status(player_cards, dealer_cards, hide_dealer_hidden_card=True):
    player_text = ("-------------------------\n"
                   f"Your cards: {player_cards}\n"
                   f"Current Score: {sum(player_cards)}\n"
                   f"\n")

    # Checks wether if dealer has blackjack before printing.
    if sum(dealer_cards) == 21:
        dealer_text = (f"Dealer's cards: {dealer_cards}\n"
                       f"Dealer's score: {sum(dealer_cards)}\n"
                       f"-------------------------")


    elif hide_dealer_hidden_card:
        dealer_text = (f"Dealer's first card: {dealer_cards[0]}\n"
                       f"-------------------------")

    else:
        dealer_text = (f"Dealer's cards: {dealer_cards}\n"
                       f"Dealer's score: {sum(dealer_cards)}\n"
                       f"-------------------------")

    return player_text + dealer_text


# List that contains both player and dealer's cards.
players_list = []
dealers_list = []

# Players Cards
first_card = random.choice(cards)
second_card = random.choice(cards)

players_list.append(first_card)
players_list.append(second_card)

# Dealers Cards
d_first_card = random.choice(cards)
d_second_card = random.choice(cards)

dealers_list.append(d_first_card)
dealers_list.append(d_second_card)

# Main logic for the game.
while playing:
    match game:
        case "yes":
            # Always adjust player status before checking rules or printing.
            while sum(players_list) > 21 and 11 in players_list:
                players_list.remove(11)
                players_list.append(1)

            # Print new lines and the logo
            print("\n" * 100)
            print(logo)
            # Prints dealers and players cards
            print(display_status(players_list, dealers_list))
            # Checks for a tie
            if sum(players_list) == 21 and sum(dealers_list) == 21:
                print("Push! Both have Blackjack.")
                playing = False
            # Checks if player has blackjack
            elif sum(players_list) == 21:
                print("Player wins with Blackjack!")
                playing = False

            elif sum(dealers_list) == 21:
                print("Dealer wins with a BlackJack!")
                playing = False

            # Checks if the player has busted
            elif sum(players_list) > 21:
                print("Player busted!")
                playing = False
            else:
                # Ask the user if they want to hit or stand.
                choice = input("Hit or Stand? ").strip().lower()
                match choice:
                    case "hit":
                        players_list.append(random.choice(cards))

                    case "stand":
                        while sum(dealers_list) > 21 and 11 in dealers_list:
                            dealers_list.remove(11)
                            dealers_list.append(1)

                        while sum(dealers_list) < 17:
                            dealers_list.append(random.choice(cards))

                            while sum(dealers_list) > 21 and 11 in dealers_list:
                                dealers_list.remove(11)
                                dealers_list.append(1)

                        # Shows the final screen.
                        print(display_status(players_list, dealers_list, hide_dealer_hidden_card=False))

                        if sum(dealers_list) > 21:
                            print("Dealer busts! Player wins!")
                        elif sum(players_list) > sum(dealers_list):
                            print("Player has the higher score! You win!")
                        elif sum(dealers_list) > sum(players_list):
                            print("Dealer has the higher score! Dealer wins!")
                        else:
                            print("Its a tie!")
                        playing = False

                    case _:
                        print("Invalid input, please try again.")

        case "no":
            print("Exiting...")
            playing = False

        case _:
            print("Invalid input, please try again.")
            playing = False
