n, q, k= map(int, input().split())
A=[]
A = list(map(int, input().split()))

def digitSUm(n):
    ans=0
    while(n!=0):
        ans += n%10
        n =n//10
    return ans


p=[]
count = 0
for i in range(n):
    if digitSUm(A[i]) == k:
        count +=1
    p.append(count)


for i in range(q):
    L, R = map(int, input().split())
    L-=1
    R-=1

    if L == 0:
        print(p[R])
    else:
        print(p[R] - p[L-1])
        


