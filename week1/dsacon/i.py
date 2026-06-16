a, b = map(int, input().split())

ca=0
cb=0
for i in range(1,int( a ** 0.5)+1):
    if(a%i==0):
        f1=i;
        f2=a//i;
        if(f1==f2):
            ca=ca+1;
        else:
            ca=ca+2;


for i in range(1,int( b ** 0.5)+1):
    if(b%i==0):
        f1=i;
        f2=b//i;
        if(f1==f2):
            cb=cb+1;
        else:
            cb=cb+2;

if (ca == cb ):
    print("DRAW")
elif(ca> cb):
    print("A")
elif(ca<cb):
    print("B")
    
