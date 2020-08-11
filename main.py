from random import randint
from time import sleep


board = ["-","-","-",
         "-","-","-",
         "-","-","-"
        ]

first_player_turn = True
turn_counter = 0


def display_board():
    print(board[0] + " |",board[1] + " | "+ board[2])
    print(board[3] + " |",board[4] + " | "+ board[5])
    print(board[6] + " |",board[7] + " | "+ board[8])
    print("\n")

def start_game():
    game = True
    while(game):
        # Win check
        game = winner_check()

        # Players turns
        turn()

        display_board()

        game = winner_check()

    if(winner == "Draw"):
        print("We got draw")

    else:
        print("Winner is "+ winner)

   
  

def winner_check():

    game3 =  diagonals_check()

    game2 = horizontal_check()

    game1 = vertical_check()

    if game1 and game2:
        return game3
    elif game2 and game3:
        return game1
    elif game1 and game3:
        return game2

def vertical_check():
    global winner
    game = True
    if(board[0] == "X" and board[3] == "X" and board[6] == "X"):
        winner = "X"
        game = False

    elif(board[1] == "X" and board[4] == "X" and board[7] == "X"):
        winner = "X"
        game = False

    elif(board[2] == "X" and board[5] == "X" and board[8] == "X"):
        winner = "X"
        game = False

    elif(board[0] == "O" and board[3] == "O" and board[6] == "O"):
        winner = "O"
        game = False

    elif(board[1] == "O" and board[4] == "O" and board[7] == "O"):
        winner = "O"
        game = False

    elif(board[2] == "O" and board[5] == "O" and board[8] == "O"):
        winner = "O"
        game = False

    return game


def horizontal_check():
    #Check horizontal rows 
    global winner
    game = True
    if(board[0] == "X" and board[1] == "X" and board[2] == "X"):
        winner = "X"
        game = False

    elif(board[3] == "X" and board[4] == "X" and board[5] == "X"):
        winner = "X"
        game = False

    elif(board[6] == "X" and board[7] == "X" and board[8] == "X"):
        winner = "X"
        game = False

    elif(board[0] == "O" and board[1] == "O" and board[2] == "O"):
        winner = "O"
        game = False

    elif(board[3] == "O" and board[4] == "O" and board[5] == "O"):
        winner = "O"
        game = False

    elif(board[6] == "O" and board[7] == "O" and board[8] == "O"):
        winner = "O"
        game = False

    return game

def diagonals_check():
    #Check diagonals
    global winner
    game = True
    if (board[0] == "X" and board[4] == "X" and board[8] == "X"):
        winner = "X"
        game = False
        
    elif(board[2] == "X" and board[4] == "X" and board[6] == "X"):
        winner = "X"
        game = False

    elif(board[0] == "O" and board[4] == "O" and board[8] == "O"):
        winner = "O"
        game = False

    elif(board[2] == "O" and board[4] == "O" and board[6] == "O"):
        winner = "O"
        game = False

    elif(turn_counter == 9):
        winner = "Draw"
        game = False
    
    return game


def turn():
    global first_player_turn
    global turn_counter
    if first_player_turn:
        poss = input("Choose from 1-9:")
        poss = int(poss) - 1

        if board[poss] == "X" or board[poss] == "O":
            print("field locked")

        else:
            # Player 1 turn x poss
            board[poss] = "X"
            first_player_turn = False
            turn_counter += 1

    else:
        # Random poss like bot 
        print("Bot turn")
        sleep(2)
        poss = randint(0,8)

        while(board[poss] == "O" or board[poss] == "X"):
            poss = randint(0,8)

        board[poss] = "O"

        first_player_turn = True

        turn_counter += 1
        

start_game()