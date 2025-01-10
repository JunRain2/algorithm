n = int(input())
numbers = list(map(int, input().split()))[:n]

operation_cnt = list(map(int, input().split()))[:4]

max_value = 0
min_value = int(1e9)


def dfs(operation_cnt, index, value):
    global max_value, min_value
    if sum(operation_cnt) == 0:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return
    for i in range(4):
        if operation_cnt[i] == 0:
            continue
        else:
            operation_cnt[i] -= 1
            if i == 0:
                tmp = value + numbers[index]
            elif i == 1:
                tmp = value - numbers[index]
            elif i == 2:
                tmp = value * numbers[index]
            elif i == 3:
                if value < 0:
                    tmp = int(-((-value) / numbers[index]))
                else:
                    tmp = int(value / numbers[index])
            dfs(operation_cnt, index + 1, tmp)
            operation_cnt[i] += 1


dfs(operation_cnt, 1, numbers[0])

print(max_value)
print(min_value)
