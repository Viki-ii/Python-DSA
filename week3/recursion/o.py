# O. Check If Array is Sorted

import sys
sys.setrecursionlimit(20**6)

n = int(input())

a = list(map(int,input().split()))

def isSorted(a, n):
    if n == 1:
        return True
    return isSorted(a, n-1) and a[n-1] >= a[n-2]

if isSorted(a, n):
    print("YES")
else:
    print("NO")