#A. Print Decreasing
import sys
sys.setrecursionlimit(10**6)

n =int(input())

def printDec(n):
    if n == 0:
        return
    print(n)
    printDec(n-1)
    

printDec(n)