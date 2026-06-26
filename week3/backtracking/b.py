# B. Climb Stairs - II




cur = []
ans = []

def f(pos, n, k):
    if pos > n:
        return
    
    if pos == n:
        ans.append(cur[:])
        return
    
    for i in range(1, k+1):
        cur.append(i)
        f(pos + i, n, k)
        cur.pop()

    

n, k = map(int, input().split())
f(0, n, k)

for x in ans:
    print(*x)