# J. All Encodings3
 
cur = []
ans = []

def f(s, idx):
    if idx == len(s):
        ans.append("".join(cur))
        return

    num = int(s[idx])
    if 1 <= num <= 9:
        cur.append(chr(num + 96))
        f(s, idx + 1)
        cur.pop()

    if idx < len(s) - 1:
        num = int(s[idx]) * 10 + int(s[idx + 1])
        if 10 <= num <= 26:
            cur.append(chr(num + 96))
            f(s, idx + 2)
            cur.pop()

s = input()

f(s, 0)

print(len(ans))
for x in ans:
    print(x)
    