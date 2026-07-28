"""
A classic BlackJack (21) card game. The player competes against the dealer to
get a hand value as close to 21 as possible without going over. It includes
features like betting, hit/stand logic, and automated dealer play.
"""

import random

# Define the basic components of a card deck
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    # Represents a single card with a suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    # Represents a deck of 52 cards
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Hand:
    # Represents the cards held by a player or dealer
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        # If total value > 21, and I still have an Ace, change Ace from 11 to 1.
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    # Keeps track of a player's starting chips and bets
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    # Asks the user for a bet amount and validates it
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, please provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, your bet can\'t exceed {chips.total}')
            elif chips.bet <= 0:
                print('Please enter a positive amount.')
            else:
                break

def hit(deck, hand):
    # Adds a card from the deck to the hand and checks for Aces
    hand.add_card(deck.deal_one())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    # Player decides whether to take another card or stop
    global playing
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ").lower()
        if x == 'h':
            hit(deck, hand)
        elif x == 's':
            print('Player stands. Dealer is playing.')
            playing = False
        else:
            print('Sorry, please try again.')
            continue
        break

def show_some(player, dealer):
    # Shows player cards and only one of the dealer's cards
    print("\nDealer's Hand:")
    print("--hidden card--")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    # Reveals all cards and their point totals
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

# Outcome functions to handle chip updates and messages
def player_busts(chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()

def player_wins(chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(chips):
    print('DEALER BUSTS!')
    chips.win_bet()

def dealer_wins(chips):
    print('DEALER WINS!')
    chips.lose_bet()

def push():
    print('Dealer and Player tie! It is a push.')

# Initialize chips outside of game loop
player_chips = Chips()

while True:
    print('\nWelcome to BlackJack!')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    take_bet(player_chips)
    show_some(player_hand, dealer_hand)

    playing = True
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    print(f"\nPlayer's total chips: {player_chips.total}")

    new_game = input('Would you like to play another hand? Enter y/n: ').lower()
    if new_game != 'y':
        print('Thanks for playing!')
        break