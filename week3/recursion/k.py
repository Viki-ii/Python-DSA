# K. Print Array

import sys
sys.setrecursionlimit(20**6)

def printArray(a, n):
    if n==0:
        return
    printArray(a,n-1)
    print(a[n-1],end=" ")
    

n=int(input())
a = list(map(int,input().split()))
printArray(a, n)
