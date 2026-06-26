

n = int(input())

board = [['.' for _ in range(n)]]
ans = []

def canPlace(row, col):

    i = row 
    j = col

    while i>=0:
        if board[i][j] == 'Q':
            return False
        i -= 1

    i = row 