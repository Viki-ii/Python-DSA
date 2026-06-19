n, m = map(int,input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if i % 2 ==0:
        for j in range(m):
            print(a[i][j], end = " ")
    else:
        for j in range(m-1,-1,-1):
            print(a[i][j], end = " ")