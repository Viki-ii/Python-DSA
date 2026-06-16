#G. Subarray with Most Primes

n, k = map(int, input().split())
a = list(map(int, input().split()))

count=0
prime = []
def isPrime(x):
    if x < 2:
        return False

    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

for s in range(n):
    if isPrime(a[s]):
        prime.append(1)
    else:
        prime.append(0)

for i in range(k):
    count+=prime[i]

best = count
start = 0

for i in range(k,n):
    count += prime[i]

    count -= prime[i-k]

    if count > best:
        best = count
        start = i-k+1
 
for i in range(start, start+k):
    print(a[i],end=" ")