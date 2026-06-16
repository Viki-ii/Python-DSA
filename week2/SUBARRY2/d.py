#D. Count Number of Distinct Integers

n, k = map(int, input().split())
a = list(map(int, input().split()))

map = {}

count = 0

for i in range(k):
    t= a[i]
    if t not in map:
        count += 1
        map[t] = 1
    else:
       map [t] += 1 
print(count, end = " ")

for i in range(k,n):
    t= a[i]
    if t not in map:
        count += 1
        map[t] = 1
    else:
       map [t] += 1 

    t= a[i-k]
    if t in map:        
        if map[t] == 1:
            count -= 1
            map.pop(t)
        else:
            map[t] -=1
    print(count, end = " ")