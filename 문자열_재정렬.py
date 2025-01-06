n = list(map(ord, input()))

n.sort()

result = ""
sum = 0
for i in range(len(n)):
    if n[i] >= ord('A'):
        result += chr(n[i])
    else:
        a = int(chr(n[i]))
        sum += a
        
print(result + str(sum))