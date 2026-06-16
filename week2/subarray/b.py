n = int(input())
a = list(map(int, input().split()))

for l in range(0,n):
    mx = a[l]
    for r in range(l,n):
        mx = max( mx, a[r])
        print(mx)