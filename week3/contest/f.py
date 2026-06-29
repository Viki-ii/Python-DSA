n = int(input())
a = list(map(int, input().split()))

ans = set()

def f(i, value):
    if i == n:
        ans.add(value)
        return

    f(i + 1, value + a[i])
    f(i + 1, value - a[i])

f(1, a[0])

print(len(ans))