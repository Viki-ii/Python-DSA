# N. Sum of the Array


import sys
sys.setrecursionlimit(20**6)

n = int(input())

a = list(map(int,input().split()))

def s(a, n):
    if n == 0:
        return 0
    return s(a, n-1) + a[n-1]
print(s(a, n))