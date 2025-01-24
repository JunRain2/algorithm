n = int(input())
array = list(map(int, input().split()))
array.sort()

result = 0
for i in range(n):
    target = array[i]
    start = 0
    end = n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        elif end == i:
            end -= 1
            continue
            
        sum_value = array[start] + array[end]
        if sum_value == target:
            result += 1
            break

        if sum_value > target:
            end -= 1
        else:
            start += 1

print(result)
