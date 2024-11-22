# simple programs level 1
# Tic Tac Toe game in Python
# Implement the functions below to make the game playable on the CLI
# You can run this file to play, run test-task1.py to test functions

# Hint: take a number to represent the players placement in the grid
# Hint: Use input (the game should be interactive)
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9

# Hint: represent the player with a variable storing a string, 'x' or 'o' 
# These can easily be used to replace the space in our 2d list board

# Hint: consider how different inputs might also break the game

#####################################################################################################
#                                  Game Logic Starts Here                                           #
#####################################################################################################

# We start with a 2d list to work with...
# the values are strings with a single space character
# this provides a good 'model' of the data in this game
board = [
    [' ', ' ' , ' '],
    [' ', ' ' , ' '],
    [' ', ' ' , ' '],
]

# CHANGE THIS TO CHANGE ICONS
def get_tile_icon(player):
    return 'X' if player == 1 else 'O'

# Function to print the game board
def print_board():
    print("Current Board: ")
    cell_value = 1
    for row in board:
        row_str = ""
        
        for i, cell in enumerate(row):
            if i > 0:
                row_str += " "
            
            #Logic that determines if cell number should be printed or user selection
            if cell == ' ':
                row_str += str(cell_value)
            else:
                row_str += str(cell)
            
            if i < len(row) - 1:
                row_str += " |"
                
            cell_value += 1
        
        print(row_str)

# Function to check if a player has won
# The current player should be provided as an argument
def check_win(player):
    for i in range(0,3):
        if board[i][0] == board[i][1] == board[i][2] != " " \
        or board[0][i] == board[1][i] == board[2][i] != " ":
            return True
        
    if board[0][0] == board[1][1] == board[2][2] != " " \
    or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Function to check if the game is a draw
def check_draw():
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return True

def get_row(position_integer):
    return (position_integer - 1) // 3

def get_col(position_integer):
    return (position_integer - 1) % 3

def set_value_in_matrix(position_integer, player):
    row = get_row(position_integer)
    col = get_col(position_integer)
    
    value = get_tile_icon(player)
    
    board[row][col] = value

def get_value_from_matrix(position_integer):
    row = get_row(position_integer)
    col = get_col(position_integer)
    return board[row][col]
    
# Main game loop
def play_game(player=1):
    
    player = player
    print(f"Player {player} it's your turn!")
    print_board()
    
    player_input = validate_input()
    set_value_in_matrix(player_input, player)
    if (check_win(player) == True):
        output(f"Player {player} won!")
        return
    if (check_draw() == True):
        output("The game ended in a tie!")
        return
        
        
    if (player == 1):
        player = 2
    else: 
        player = 1
        
    play_game(player)

def check_valid_placement(position):
    return get_value_from_matrix(position) == ' '

def validate_input():
    while True:
        try:
            player_selection = int(input("Enter the number tile you want to go in (1-9): "))
            
            if player_selection < 1 or player_selection > 9:
                output("Invalid input! Please enter a number between 1 and 9.")
                continue

            if not check_valid_placement(player_selection):
                output("Sorry, that spot is already taken! Please choose a different spot.")
                continue
            
            return player_selection

        except ValueError:
            output("Invalid input! Please enter a valid number between 1 and 9.")
            
            
#Wrapper print method which includes a new line to make console look clearer
def output(x):
    print(f"{x} \n")
    

#Entry point
if __name__ == '__main__':
    play_game()