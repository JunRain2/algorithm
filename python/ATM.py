n = int(input())

array = list(map(int,input().split()))

array.sort()

total = 0
tmp = 0
for i in array:
    tmp += i
    total += tmp
    
print(total)
    