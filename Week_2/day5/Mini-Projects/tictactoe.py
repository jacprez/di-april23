# # Tic Tac Toe Game

# Make the board:
# [_ , _ , _ ]
# [_ , _ , _ ]
# [_ , _ , _ ]

# Access the row:
    
    
    
# print the board - create a function


# player_input()
# maximum turn is 9 

# if the turn is 1 then it should be X and if the turn is 2 it should be O

# can use a while loop such as while turns < maximum_turn


# need an input from the user of row and column



# for row in board:
#     print(row[0] + ' |' + row[1] + ' |' + row[2] + ' |')
    

# check_win()
#     insert if statements to check 

# Globla Variables
board = [' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ',
        ' - ', ' - ', ' - ']
game_still_going = True

winner = None

current_player = 'X'

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')


def play_game() :
    display_board() #first is to display the board
    
    while game_still_going :
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()

# The game is over
    if winner == 'X' or winner == 'O':
        print(f'{winner} won!')
    elif winner == None:
        print('Its a tie.')


def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    
    board[position] = 'X'
    display_board()


def check_if_game_over():
    check_for_winner()
    check_tie()
    
def check_for_winner():
    #check rows, col, and diag
    return

def check_rows():
    return

def check_columns():
    return

def check_diagonals():
    return

def check_tie():
    return

def flip_player():
    return

play_game()