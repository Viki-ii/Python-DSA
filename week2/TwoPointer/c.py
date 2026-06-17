#C. Longest Substring Without Repeating Characters

n = int(input())

s = input()

ans = 0

dict ={}
l=0
for r in range(n):
    if s[r] in dict:
        dict[s[r]]+=1
    else:
        dict[s[r]] = 1

    while dict[s[r]] > 1:
        dict[s[l]]-=1

        if dict[s[l]] == 0:
            del(dict[s[l]])

        l+=1

    ans = max(ans, r-l+1)
print(ans)