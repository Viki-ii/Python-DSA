#F. Maximum Balanced Window

n, k = map(int,input().split())
a = list(map(int, input().split()))


ones = 0
for i in range(k):
    ones += a[i]
ans = min(k, ones+1)  
for i in range(k, n):
    ones += a[i]
    ones -= a[i-k]

    ans = max(ans, min(k,ones+1))
print(ans)
