#A. The Intern Who Pushed to Main

n = int(input())
a = list(map(int, input().split()))

for l in range(n):
    maxm = a[l]
    for r in range(l,n):
        maxm = max(maxm, a[r])
        print(maxm, end =" ")