# D. Print Number in Reverse


import sys
sys.setrecursionlimit(10**6)

def printReverse(n):
    if n==0:
        return
    print (n % 10, end ="")
    printReverse(n // 10)

n = int(input())
if n == 0:
    print(0)
else:
    printReverse(n)