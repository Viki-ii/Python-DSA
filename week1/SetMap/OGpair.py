s = input()
n = len(s)
ans = 0
cnt = 0

for j in range(n):
    if s[j] == "G":
        ans += cnt
    elif s[j] == "O":
        cnt+=1
print(ans)
