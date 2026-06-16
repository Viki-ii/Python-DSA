n, k = map(int, input().split())
a = input()

count = 0

def isVowel(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    if(s in vowels):
        return True
    return False



for i in range(k):
    if isVowel(a[i]):
        count += 1


print(count, end = " ")

for i in range(k,n):
    if isVowel(a[i]):
        count += 1

    if isVowel(a[i-k]):
        count -= 1

    print(count, end = " ")
    
