#F. Count Streaks
n = int(input())
a = list(map(int, input().split()))

s = set()
l = 0
ans = 0

for r in range(n):
    while a[r] in s:
        s.remove(a[l])
        l += 1

    s.add(a[r])
    ans += r - l + 1

print(ans)