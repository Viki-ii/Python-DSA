# j. Print reverse Array
import sys
sys.setrecursionlimit(20**6)

def printArray(a, n):
    if n==0:
        return
    print(a[n-1],end=" ")
    printArray(a,n-1)

n=int(input())
a = list(map(int,input().split()))
printArray(a, n)
