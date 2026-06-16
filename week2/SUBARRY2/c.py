#C. Count Good Numbers

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
good = set(list(map(int, input().split())))

count = 0 
for i in range(k):
    if a[i] in good:
        count +=1
print(count, end = " ")
    
for i in range(k,n):
    
    if a[i] in good:
        count += 1
    
    if a[i-k] in good:
        count -=1
    print(count, end = " ")
