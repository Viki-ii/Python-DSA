n, x = map( int, input().split())
a = list(map(int,input().split()))



def checkpair():
    freq = {}
    cnt = 0
    for j in range(n):
        req = x - a[j] 

        if req in freq:
            cnt += freq[req]

        if a[j] in freq:
            freq[a[j]] += 1
        else:
            freq[a[j]] = 1
        
        
    return cnt

ans = checkpair()
  
print(ans)