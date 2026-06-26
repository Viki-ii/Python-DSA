import sys
sys.setrecursionlimit(10**6)


cur = []
ans = []

def f(idx):
    if idx == n:
        if cur:
            print(*cur)
        return
    f(idx+1)

    cur.append(a[idx])
    f(idx+1)
    cur.pop()



    
n = int(input())
a = list(map(int, input().split()))
f(0)

