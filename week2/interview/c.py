#C. Boundary Traversal

n, m = map(int,input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for j in range(m):
    print(a[0][j], end = " ")

for i in range(1, n):
    print(a[i][m-1], end=" ")

if n > 1 :
    for j in range(m-2,-1,-1):
        print(a[n-1][j], end=" ")

if m>1:
    for i in range(n-2,0,-1):
        print(a[i][0], end = " ")

