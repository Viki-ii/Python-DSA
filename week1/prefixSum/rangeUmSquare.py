n, q= map(int, input().split())
A=list( map( int, input().split() ))

p=[]
sum=0
for i in range(n):
    sum += A[i] * A[i]    
    p.append(sum)



for i in range(q):
    L, R = map(int, input().split())
    L-=1
    R-=1

    if L == 0:
        print(p[R])
    else:
        print(p[R] - p[L-1])
