cur = []
ans = []

def f(a, idx, sum):
    if idx == n:
        if sum == k:
            ans.append(cur[:])
        return
    f(a, idx+1, sum)

    cur.append(a[idx])
    f(a,idx+1,sum + a[idx])
    cur.pop()



    
n, k = map(int,input().split())
a = list(map(int, input().split()))
f(a, 0, 0)

for x in ans:
    if len(x) >0:
        print(*x)