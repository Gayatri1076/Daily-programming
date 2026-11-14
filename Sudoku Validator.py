board = []

print("Enter 9 rows with 9 numbers each:")

for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)

valid = True

for i in range(9):
    if len(set(board[i])) != 9:
        valid = False

for j in range(9):
    column = [board[i][j] for i in range(9)]
    if len(set(column)) != 9:
        valid = False

if valid:
    print("Rows and columns are valid!")
else:
    print("Invalid Sudoku!")