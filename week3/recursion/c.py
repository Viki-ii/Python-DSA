#C. Print Zig Zag


import sys
sys.setrecursionlimit(10**6)


n =int(input())

def printDec(n):
    if n <= 0:
        return
    print(n)
    printDec(n-1)
    if n!=1:
        print(n)
    

printDec(n)