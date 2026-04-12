"""
A console-based Tic-Tac-Toe game for two players. Players choose X or O,
take turns selecting positions on the board, and the game checks for wins,
ties, and replay options.
"""
# Clear some space in the console
print("\n" * 10)

# Function to print the current state of the board
def display_board(board):
    print("["+ board[1]+ "]["+board[2]+"]["+board[3]+ "]")
    print("["+ board[4]+ "]["+board[5]+"]["+board[6]+ "]")
    print("["+ board[7]+ "]["+board[8]+"]["+board[9]+ "]")

# Function to let Player 1 choose their marker (X or O)
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function to assign a marker to a specific index on the board list
def place_marker(board, marker, position):
    board[position] = marker

# Function to check all possible winning combinations
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

import random

# Function to randomly decide which player starts first
def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

# Function to check if a specific spot on the board is empty
def space_check(board, position):
    return board[position] == ' '

# Function to check if the entire board is filled (a tie)
def full_board_check(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True

# Function to get the player's next move and validate it
def player_choice(board):
    choice_input = 0 
    while choice_input not in [1,2,3,4,5,6,7,8,9] or not space_check(board, choice_input):
        choice_input = int(input("Enter your next position (1-9): "))
    return choice_input

# Function to ask players if they want to restart the game
def ask_to_play_again():
    response = input("Do you want to play again? [Yes or No]: ")
    return response.lower() == "yes"

# Main Game Engine
while True:
    # Initialize an empty board
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    
    # Decide who goes first
    turn = choose_first()
    print(turn + " will go first.")
    
    play_game_response = input("Want to play? [Yes or No] ")
    game_active = (play_game_response.lower() == "yes")

    while game_active:
        if turn == "Player 1":
            # Player 1 Logic
            display_board(the_board)
            selected_position = player_choice(the_board)
            place_marker(the_board, player1_marker, selected_position)

            # Check for win or tie
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 HAS WON!!")
                print("Thank's for playing the game.")
                game_active = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    print("Thank's for playing the game.")
                    game_active = False
                else:
                    turn = "Player 2"
        else:
            # Player 2 Logic
            display_board(the_board)
            selected_position = player_choice(the_board)
            place_marker(the_board, player2_marker, selected_position)

            # Check for win or tie
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 HAS WON!!")
                print("Thank's for playing the game.")
                game_active = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    print("Thank's for playing the game.")
                    game_active = False
                else:
                    turn = "Player 1"

    # Break out of the loop if they don't want to play again
    if not ask_to_play_again():
        break
