n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

# Left column
for i in range(n - 1, -1, -1):
    if a[i][0] == -1:
        exit()
    print(a[i][0], end=" ")

# Top row
for j in range(1, m):
    if a[0][j] == -1:
        exit()
    print(a[0][j], end=" ")

# Right column
for i in range(1, n):
    if a[i][m - 1] == -1:
        exit()
    print(a[i][m - 1], end=" ")

# Bottom row
for j in range(m - 2, 0, -1):
    if a[n - 1][j] == -1:
        exit()
    print(a[n - 1][j], end=" ")