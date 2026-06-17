#E. Count Subarrays with At Most K Distinct

n, k = map(int, input().split())

s = list(map(int,input().split()))

ans = 0

dict ={}
l=0
for r in range(n):
    if s[r] in dict:
        dict[s[r]]+=1
    else:
        dict[s[r]] = 1

    while len(dict) > k:
        dict[s[l]]-=1

        if dict[s[l]] == 0:
            del(dict[s[l]])

        l+=1

    ans += r-l+1
print(ans)