#E. Factorial


import sys
sys.setrecursionlimit(10**6)

def facto(n):
    if n == 0:
        return 1
    return facto( n - 1 ) * n
print(facto(int(input())))