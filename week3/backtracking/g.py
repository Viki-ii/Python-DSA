#G. Generate Parentheses
n = int(input())

cur = []
ans = []

def f(open , close):
    if close == n :
        ans.append("".join(cur))
        return
    if open<n:
        cur.append('(')
        f(open+1, close)
        cur.pop()

    if open> close:            
        cur.append(')')
        f(open, close+1)
        cur.pop()

f(0, 0)

print(len(ans))
for i in ans:
    print(i)