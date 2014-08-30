import time

FREE = "-"
BLOCKED = "*"
QUEEN = "Q"

UP = -1
LEFT = -1
DOWN = 1
RIGHT = 1

# Global Variables
board = []
b_stack = []  # Boards stack
N = 4         # Board size is N * N
n_queens = 0  # number of queens placed

def init_board():
    for i in range(0, (N*N) + 1):
        board.append(FREE)

# Creates a copy of current board
# and adds it to the stack.
# Then, place a queen on the board(not the copy)
def place_queen(row, col):
    global board
    global b_stack
    global n_queens

    b_stack.insert(0,list(board)) # clone current board/state and add it to the stack

    board[N*row + col] = QUEEN
    n_queens += 1
    mark_path(row, col)

def mark_path(row, col):
    for i in range(row, N): # mark rows down
        if(board[N*i + col] != QUEEN):
            board[N*i + col] = BLOCKED
    for j in range(col, N): # mark collumns right
        if(board[N*row + j] != QUEEN):
            board[N*row + j] = BLOCKED

    for i in range(0, row): # mark rows up
        if(board[N*i + col] != QUEEN):
            board[N*i + col] = BLOCKED

    for j in range(0, col): # mark collumns left
        if(board[N*row + j] != QUEEN):
            board[N*row + j] = BLOCKED

    block_diagonal(row, col, UP, RIGHT)
    block_diagonal(row, col, UP, LEFT)
    block_diagonal(row, col, DOWN, LEFT)
    block_diagonal(row, col, DOWN, RIGHT)

def block_diagonal(row, col, row_dir, col_dir):
    while((row < N and col < N) and (row >= 0 and col >= 0) and
          (row < N and col >= 0) and (row >= 0 and col < N)):

        if(board[N*row + col] != QUEEN):
            board[N*row + col] = BLOCKED;
        row += row_dir;
        col += col_dir;


# Goes back to the previous board state.
# Used to remove a Queen of the board
def backtrack():
    global board
    global n_queens

    board = list(b_stack.pop(0))
    n_queens -= 1

def valid_pos(row, col):
    return(board[N*row + col] == FREE)

def get_queen_col(row):
    for i in range(0, N):
        if(board[N*row + i] == QUEEN):
            return i

def print_board():
    global board

    count = 0
    for i in range(0, N*N):
        if(count == N):
            count = 0
            print()
        if(board[i] == QUEEN):
            print(QUEEN, "", end="")
        elif(board[i] == FREE):
            print(FREE, "", end="")
        else:
            print(board[i], "", end="")
        count += 1
    print()

def main():
    global board
    global n_queens

    row = 0
    col = 0

    init_board()

    start_t = time.time()
    while(n_queens != N):
        if(col == N): # means that the whole row is attacked
            row -= 1 # go to the row of the last placed queen
            col = get_queen_col(row) + 1 # start from the column of the last placed queen, + 1
            backtrack()
        elif(valid_pos(row, col)):
            place_queen(row,col)
            row += 1
            col = 0
        else:
            col += 1
    elap_t = (time.time() - start_t)

    print_board()
    print("Elapsed Time: ", "{:.2e}".format(elap_t), " seconds")

if __name__ == "__main__":
    main()
