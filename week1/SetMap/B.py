n, q = map(int, input().split())
a = list(map(int, input().split()))

freq = {}
for i in range(n):
    freq[ a[i] ] = i+1

for i in range( q ):
    x = int(input())
    if x in freq:
        print(freq[x])
    else:
        print(-1)
