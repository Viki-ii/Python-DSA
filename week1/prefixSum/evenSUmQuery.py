n=int( input() )
A=list( map( int, input().split() ))

p=[]
sum=0
for i in range(n):
    if i%2!=0 :
        sum += A[i]
    else:
        sum+=0
    
    p.append(sum)


q=int(input())
for i in range(q):
    L, R = map(int, input().split())
    L-=1
    R-=1

    if L == 0:
        print(p[R])
    else:
        print(p[R] - p[L-1])
