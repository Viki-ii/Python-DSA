n = int(input())
a = list(map (int, input().split()))

for l in range(0,n):
    for r in range(l,n):
        for i in range(l,r+1):
            print(a[i],end=" ")
        print()