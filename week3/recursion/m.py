# M. Maximum Element


import sys
sys.setrecursionlimit(20**6)

n = int(input())
a = list(map(int,input().split()))

def findMax(a, n ):
    if n==1:
        return a[0]
    smallAns = findMax(a, n-1)
    return max(smallAns, a[n - 1])

print(findMax(a, n))