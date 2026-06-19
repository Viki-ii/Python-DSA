#B. COunt Subarrays

n = int(input())
a = list(map(int, input().split()))
k = int(input())

ans = 0

l=0

for r in range(n):
    s=0
    for j in range(r,n):
        s+= a[j]
        if s == k:
            ans+=1
            

print(ans)