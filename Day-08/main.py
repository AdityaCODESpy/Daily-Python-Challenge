# Day-08/main.py
import random

board = [" " for _ in range(9)]

def print_board():
    print("\n  |   |  ")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("  |   |  ")
    print("---------")
    print("  |   |  ")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("  |   |  ")
    print("---------")
    print("  |   |  ")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("  |   |  \n")

def check_win(player):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a,b,c in win_conditions)

def play_tictactoe():
    print("TIC TAC TOE — Tu = X, Computer = O")
    print_board()
    
    while True:
        # User turn
        pos = int(input("Position daal (1-9): ")) - 1
        if board[pos] == " ":
            board[pos] = "X"
        else:
            print("Wahan pehle se hai!")
            continue
            
        print_board()
        if check_win("X"):
            print("TU JEET GAYA!")
            break
        if " " not in board:
            print("DRAW!")
            break
            
        # Computer turn
        comp = random.choice([i for i, x in enumerate(board) if x == " "])
        board[comp] = "O"
        print("Computer ne daala:", comp+1)
        print_board()
        if check_win("O"):
            print("COMPUTER JEET GAYA!")
            break

play_tictactoe()