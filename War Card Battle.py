"""
A two-player War card game simulation. A deck is created, shuffled, and
split between two players. Each round, players draw cards and compare
values. Ties trigger 'war' where additional cards are drawn until a
winner is determined. The game continues until one player runs out of cards.
"""

import random

# Global variables for card setup
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11, "Queen":12, "King":13, "Ace":14}

class Card:
    #Represents a single playing card.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    #Represents a deck of 52 cards.
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_desk(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    #Represents a player with a hand of cards.
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # Remove card from the top of the deck i.e. index 0.
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        # Handle adding multiple cards (list) or a single card
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_desk()

# Split the deck
for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on = True
round_num = 0

# Main Game Loop
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    # Check for game over conditions
    if len(player_one.all_cards) == 0:
        print("Player One is out of cards! Player Two Has won!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two is out of cards! Player One Has won!")
        game_on = False
        break

    # Start a new round - cards currently on the table
    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    at_war = True
    while at_war:
        # Player One wins the round
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False

        # Player Two wins the round
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False

        # War scenario
        else:
            print("WAR!!")
            # Check if players have enough cards to declare war (3 additional cards)
            if len(player_one.all_cards) < 3:
                print("Player One unable to declare a war. Player Two Wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("Player Two unable to declare a war. Player One Wins!")
                game_on = False
                break
            else:
                # Draw 3 additional cards for the war
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
