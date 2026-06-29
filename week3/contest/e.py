
cur = []


def f(c_sum):
    if c_sum == K:
        print(*cur)
        return
    if c_sum > K:
        return
    
    for i in range(1, 7):
        cur.append(i)
        f(c_sum+i)
        cur.pop()

K = int(input())



f(0)
