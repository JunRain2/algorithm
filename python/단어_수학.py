n = int(input())
words = [list(input()) for _ in range(n)]

value = [0] * 26
for word in words:
    for i, c in enumerate(word):
        value[ord(c) - ord('A')] += 10 ** (len(word) - 1 - i)
        
value.sort(reverse = True)
result = 0
for i, v in enumerate(value):
    result += v * (9 - i)
    
print(result)