board = [list(input()) for _ in range(9)]


def canPlace(val, row, col):
    for j in range(9):
      if board[row][j] == val:
         return False

    for i in range(9):
      if board[i][col] == val:
         return False
      
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    for i in range(3):
      for j in range(3):
         if board[startRow + i][startCol + j] == val:
            return False
         
    return True



def f(row, col):
    if col == 9:
        return f(row+1, 0)
    
    if row == 9:
        return True
    
    if board[row][col] != '.':
        return f(row, col+1)
    
    for num in range(1,10):
        val = str(num)
        if canPlace(val, row,col):
            board[row][col] = val
        
            if f(row, col+1):
               return True
            
            board[row][col] = '.'
    return False

f(0, 0)

for row in board:
   print("".join(row))