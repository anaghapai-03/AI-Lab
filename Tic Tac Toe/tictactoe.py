import random


board = [" "] * 9
win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]

def print_board():

    print(f"\n [{board[0]}]  [{board[1]}]  [{board[2]}] \n [{board[3]}]  [{board[4]}]  [{board[5]}] \n [{board[6]}]  [{board[7]}]  [{board[8]}] \n")

def check_win(player):

    return any(board[a] == board[b] == board[c] == player for a, b, c in win_positions)


print("choose 1-9.")
print_board()

for turn in range(9):
    if turn % 2 == 0:
        move = int(input("choose (1-9): ")) - 1
        while board[move] != " ":
            move = int(input("choose another: ")) - 1
        board[move] = "X"
    else:
        print("filled")

        empty = [i for i, x in enumerate(board) if x == " "]
        move = None


        for p in ["O", "X"]:
            for i in empty:
                board[i] = p
                if check_win(p): move = i
                board[i] = " "
            if move is not None: break

        if move is None: move = random.choice(empty)
        board[move] = "O"

    print_board()

    if check_win("X"):
        print("A won")
        break
    if check_win("O"):
        print("B won")
        break
else:
    print("draw")
