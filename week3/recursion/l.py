# L. Minimum Element


import sys
sys.setrecursionlimit(20**6)

n = int(input())
a = list(map(int,input().split()))

def findMin(a, n ):
    if n==1:
        return a[0]
    smallAns = findMin(a, n-1)
    return min(smallAns, a[n - 1])

print(findMin(a, n))