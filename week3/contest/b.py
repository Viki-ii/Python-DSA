def f(n):
    if n == 0:
        return A 
    if n == 1:
        return B 
    if n == 2:
        return C 
    return f(n-1) + f(n-3)

A, B, C, n = map(int, input().split())

print(f(n))