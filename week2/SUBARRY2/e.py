#E. Good Subarrays

n, k, t = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
sum = 0

for i in range(k):
    sum += a[i]

if (sum // k) >= t:
    ans+=1
for i in range(k,n):
    sum+= a[i]
    sum-= a[i-k]

    if sum // k >= t:
        ans+=1
print(ans)

