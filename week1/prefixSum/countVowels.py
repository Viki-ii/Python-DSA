n=int( input() )
A=input()

vowels = {'a', 'e', 'i', 'o', 'u'}


p = [0] * n
cnt = 0

for i in range(n):
    if A[i] in vowels:
        cnt += 1
    p[i] = cnt


q=int(input())
for i in range(q):
    L, R = map(int, input().split())
    L-=1
    R-=1

    if L == 0:
        print(p[R])
    else:
        print(p[R] - p[L-1])
