# A. Count Zeroes

def zero(n):
    if n < 10:
        if(n==0):
            return 1
        return 0


    if n%10 == 0:
        return 1 + zero(n//10)
    else:
        return zero(n//10)

     
n=int(input())

print(zero(n))
    