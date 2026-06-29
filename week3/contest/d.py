def sum(n):
    ans = 0
    while(n!=0):
        ans += n%10
        n //=10
    return ans



def magic(n):
    if n< 10:
        return n
    
    return magic(sum(n))

n = int(input())
print(magic(n))
    