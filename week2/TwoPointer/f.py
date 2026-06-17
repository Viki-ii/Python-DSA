#F. Smallest Subarray with Sum > K

n, k = (map(int, input().split()))
a = list(map(int, input().split()))

l=0
sum = 0
ans= n+1
for r in range(n):
    sum += a[r]
    while sum > k:
        ans = min(ans, r-l+1)
        sum -= a[l]
        l += 1
        
if ans == n+1:
    print(-1)
else:
    print(ans)