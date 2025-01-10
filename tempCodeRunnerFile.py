n = int(input())
numbers = list(map(int, input().split()))[:n]

operation = ["+", "-", "*", "/"]
operation_cnt = list(map(int, input().split()))[:4]

max_value = 0
min_value = int(1e9)


def dfs(operation_cnt, index, value):
    global max_value, min_value
    if sum(operation_cnt) == 0:
        return value
    for i in range(4):
        if operation_cnt[i] == 0:
            continue
        else:
            operation_cnt[i] -= 1
            if operation[i] == "+":
                value = int(value + numbers[index])
            elif operation[i] == "-":
                value = int(value - numbers[index])
            elif operation[i] == "*":
                value = int(value * numbers[index])
            elif operation[i] == "/":
                value = int(value / numbers[index])
            result = dfs(operation_cnt, index + 1, value)
            max_value = max(max_value, result)
            min_value = min(min_value, result)


dfs(operation_cnt, 1, numbers[0])

print(max_value, min_value)
