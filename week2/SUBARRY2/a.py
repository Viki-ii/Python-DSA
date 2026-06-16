n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0

for i in range(k):
    sum += a[i]

ans = sum

for i in range(k,n):
    sum += a[i]
    sum -= a[i-k]

    ans = max(ans, sum)
print(ans)