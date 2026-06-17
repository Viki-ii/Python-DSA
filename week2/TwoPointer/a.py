#A. Longest Subarray with Sum < K

n, k = (map(int, input().split()))
a = list(map(int, input().split()))

l=0
sum = 0
ans=0
for r in range(n):
    sum += a[r]
    while sum >= k:
        sum -= a[l]
        l += 1

    ans = max(ans, r-l+1)
print(ans)