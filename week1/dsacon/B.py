n = int (input())
L = list(map(int,input().split())) 

s=set()

for i in L:
    if (i in s):
        
        print("NO",end = " ")
    else:
        print("YES",end = ' ')
        s.add(i)