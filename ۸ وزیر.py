
def is_safe(board, row, col):
  # Check this column on upper side
  for i in range(row):
     if board[i] == col or \
        board[i] - i == col - row or \
        board[i] + i == col + row:
          return False
  return True

def print_board(board):
   n = len(board)
   for row in range(n):
       line = ""
   for col in range(n):
       if board[row] == col:
          line += "Q "
   else:
       line += ". "
       print(line)
   print("\n")

def solve_n_queens(n, row=0, board=None):
  if board is None:
     board = [-1] * n
  if row == n:
     print_board(board)
     return True
  for col in range(n):
     if is_safe(board, row, col):
       board[row] = col
     if solve_n_queens(n, row + 1, board):
          return True
     board[row] = -1
  return False

# Run the program with 8 queens
solve_n_queens(8)
