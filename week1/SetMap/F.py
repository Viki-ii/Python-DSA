n, x = map(int, input().split())
a = list(map(int, input().split()))

st = set()

def checkpair(st):
    for j in range(n):
        req = x - a[j] 

        if req in st:
            return "TRUE" 
        
        st.add(a[j])
    return "FALSE"

   
print(checkpair(st))