q = int( input() )

freq = {}

for i in range(q):
    n, x = map( int, input().split() )

    if( n == 1 ):
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    elif n == 2 :
        if x in freq:
            freq[x] -= 1
            if freq[x] == 0:
                del freq[x]
    elif n == 3 :
        if x in freq:
            print(freq[x])
        else:
            print(0)
