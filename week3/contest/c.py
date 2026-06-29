import sys
sys.setrecursionlimit(10**6)

def zigzagArray(a, n):
    if n<0:
        return 
    
    print(a[n], end = " ")
    zigzagArray(a,n-1)
    if n >0:
        print(a[n], end = " ")

n = int(input())   
a = list(map(int, input().split())) 

zigzagArray(a, n-1)