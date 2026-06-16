n, q = map(int, input().split())
s = input()

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

p = [0] * (n + 1)

for i in range(n):
    p[i + 1] = p[i]
    if s[i] in vowels:
        p[i + 1] += 1

for j in range(q):
    L, R = map(int, input().split())

    vowelCount = p[R] - p[L - 1]
    length = R - L + 1

    if 2 * vowelCount == length:
        print("YES")
    else:
        print("NO")