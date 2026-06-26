# P. First Occurence of X

import sys
sys.setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

x= int(input())

def firstOcc(a, n, x):
    if n == 0:
        return -1
    smallAns = firstOcc(a, n-1, x)

    if smallAns != -1:
        return smallAns
    return n if a[n-1] == x else -1

print(firstOcc(a, n, x))