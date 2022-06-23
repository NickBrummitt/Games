"""
We will need functions for a few things:
1) A board
2) Display the board
3) Play the game
4) Check if a player has won
    i) Check rows
    ii) Check columns
    iii) Check diagonals
5) Check if the game was a tie
6) Flip player control
7) Handling a turn (inputs)
"""

# --- Global Variables ---#

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_on = True

# Who won? Or tie?
winner = None

# Whose turn is it?
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of TicTacToe
def play_game():
    # Display initial board
    display_board()

    # While the game is still going
    while game_on:

        # Handle a single turn of a arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie.")


# Check if the game is over
def check_game_over():
    check_winner()
    check_tie()


# Check for a winner
def check_winner():

    # Set up global variables
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_columns()

    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


# Check rows for a winner
def check_rows():

    # Set up global variables
    global game_on

    # Check each row starting from the top
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # Stop the game if there is a winning row
    if row_1 or row_2 or row_3:
        game_on = False

    # Get winning player
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


# Check columns for a winner
def check_columns():

    # Set up global variables
    global game_on

    # Check each column starting from the left
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # Stop the game if there is a winning row
    if column_1 or column_2 or column_3:
        game_on = False

    # Get winning player
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


# Check diagonals for a winner
def check_diagonals():

    # Set up global variables
    global game_on

    # Check both diagonals
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # Stop the game if there is a winning row
    if diagonal_1 or diagonal_2:
        game_on = False

    # Get winning player
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return


# Check for a tie
def check_tie():
    # Set up global variables
    global game_on

    if "-" not in board:
        game_on = False
    return


# Flip to the other player
def flip_player():
    # Set global variables
    global current_player

    # Switch to opposite player character
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return


# Handle a single turn of an arbitrary player
def handle_turn(player):
    print(player + "'s turn...")

    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        # Write character to game board
        position = int(position) - 1

        # Catch overwriting existing turns
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again!")

    board[position] = player
    display_board()

play_game()