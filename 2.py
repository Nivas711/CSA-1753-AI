N = 8
board = [-1] * N

def is_safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False

def print_board():
    for i in range(N):
        row = ['1' if board[i] == j else '.' for j in range(N)]
        print(' '.join(row))

if solve(0):
    print_board()
else:
    print("No solution exists")
