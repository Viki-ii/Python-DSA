#D. Distinct Numbers in Window

n= int(input())
a = list(map(int, input().split()))
k = int(input())

freq = {}
for i in range(k):
    if a[i] in freq:
        freq[a[i]] +=1
    else:
        freq[a[i]] = 1
print(len(freq), end= " ")

for i in range(k,n):
    if a[i] in freq:
        freq[a[i]] +=1
    else:
        freq[a[i]] = 1
    
    if a[i-k] in freq:
        freq[a[i-k]] -=1
        if freq[a[i-k]] == 0:
            del freq[a[i-k]]
    print(len(freq), end= " ")