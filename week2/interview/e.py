#. Spiral Matrix

n, m = map(int,input().split())

a = [list(map(int, input().split())) for _ in range(n)]

startRow =0 
endRow = n -1
startCol = 0
endCol = m-1

def printBoundary(a, startRow, endRow, startCol, endCol):
    for j in range(startCol, endCol+1):
        print(a[startRow][j], end = " ")

    for i in range(startRow+1,endRow+1):
        print(a[i][endCol], end=" ")

    if startRow!=endRow :
        for j in range(endCol-1,startCol-1,-1):
            print(a[endRow][j], end=" ")

    if startCol != endCol:
        for i in range(endRow-1,startRow,-1):
            print(a[i][startCol], end = " ")




while(startRow<=endRow and startCol <= endCol):
    printBoundary(a, startRow, endRow, startCol, endCol)

    startRow+=1
    endRow-=1
    startCol+=1
    endCol -= 1
