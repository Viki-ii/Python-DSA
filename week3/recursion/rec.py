def zigzag(n):
    if n == 0:
        return
    print(n)
    zigzag(n-1)
    if n!=1:
        print(n)

zigzag(int(input()))


# print number in reverse

# def printReverse(n):
#     if n==0:
#         return
#     print (n%10,end ="")
#     printReverse(n//10)

# printReverse(int(input()))

#power

def printPower(x, n):

    if n == 0:
        return 1
    

    return printPower(x,n-1) * x
print(printPower(3,3))