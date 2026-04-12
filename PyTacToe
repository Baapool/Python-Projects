"""
A console-based Tic-Tac-Toe game for two players. Players choose X or O,
take turns selecting positions on the board, and the game checks for wins,
ties, and replay options.
"""

print("\n" * 10)
def display_board(board):
    print("["+ board[1]+ "]["+board[2]+"]["+board[3]+ "]")
    print("["+ board[4]+ "]["+board[5]+"]["+board[6]+ "]")
    print("["+ board[7]+ "]["+board[8]+"]["+board[9]+ "]")

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

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

def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True

def player_choice(board):

    choice_input = 0 # Renamed local variable 'position' to 'choice_input'

    while choice_input not in [1,2,3,4,5,6,7,8,9] or not space_check(board, choice_input):
        choice_input = int(input("Enter your next position (1-9): "))


    return choice_input

def ask_to_play_again(): # Renamed the function to avoid clash
    response = input("Do you want to play again? [Yes or No]: ")
    return response.lower() == "yes"


while True:
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + " will go first.")

    play_game_response = input("Want to play? [Yes or No] ")
    game_active = (play_game_response.lower() == "yes") # Use a new boolean variable for game state


    while game_active:
        if turn == "Player 1":
            display_board(the_board)
            selected_position = player_choice(the_board) # Renamed 'position' to 'selected_position'
            place_marker(the_board, player1_marker, selected_position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 HAS WON!!")
                print("Thank's for playing the game.")
                game_active = False # Corrected assignment








            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    print("Thank's for playing the game.")
                    game_active = False # Corrected assignment


                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            selected_position = player_choice(the_board) # Renamed 'position' to 'selected_position'
            place_marker(the_board, player2_marker, selected_position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 HAS WON!!")
                print("Thank's for playing the game.")
                game_active = False # Corrected assignment





            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a Tie")
                    print("Thank's for playing the game.")
                    game_active = False # Corrected assignment

                else:
                    turn = "Player 1"


    if not ask_to_play_again(): # Call the renamed function to check if another game should be played
        break
