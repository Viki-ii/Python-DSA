#B. Wave - II

n, m = map(int,input().split())

a = [list(map(int, input().split())) for _ in range(n)]

for j in range(m):
    if j % 2 ==0:
        for i in range(n):
            print(a[i][j], end = " ")
    else:
        for i in range(n-1,-1,-1):
            print(a[i][j], end = " ")