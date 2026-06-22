# F. Sum of first N Natural Numbers

import sys
sys.setrecursionlimit(10**6)

def sum1ToN(n):
    if n == 0:
        return 0
    return sum1ToN(n-1) + n

print(sum1ToN(int(input())))