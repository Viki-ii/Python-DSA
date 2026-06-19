n, k, t = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a[:k])
ans = 0

if s >= k * t:
    ans += 1

for i in range(k, n):
    s += a[i]
    s -= a[i - k]

    if s >= k * t:
        ans += 1

print(ans)