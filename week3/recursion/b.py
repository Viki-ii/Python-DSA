#B. Print Increasing

import sys
sys.setrecursionlimit(10**6)


n =int(input())

def printDec(n):
    if n <= 0:
        return
    
    printDec(n-1)
    print(n)
    

printDec(n)