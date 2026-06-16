q = int( input() )

freq = {}

for i in range(q):
    a = list(map( int, input().split() ))

    if( a[0] == 1 ):
        x = a[1]
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    elif a[0] == 2 :
        x = a[1]
        if x in freq:
            del freq[x]
    elif a[0] == 3:
        
        print(len(freq))
    elif a[0] == 4 :
        x = a[1]
        if x in freq:
            print("YES")
        else:
            print("NO")
