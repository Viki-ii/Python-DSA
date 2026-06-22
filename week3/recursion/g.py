# G. Power

import sys
sys.setrecursionlimit(10**6)


x, n = map(int,input().split())

def power(x,n):
    if n == 0:
        return 1
    return power(x, n-1) * x

print(power(x, n))