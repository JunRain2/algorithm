def switch(data, i, n):
    for j in range(i - 1, i + 2):
        if 0 <= j < n:
            data[j] = 1 - data[j]

def try_solve(data, n):
    result = 0
    for i in range(1, n):
        if data[i - 1] != array[i - 1]:
            result += 1
            switch(data, i, n)
    return result if data == array else -1

n = int(input())
data = list(map(int, input()))
array = list(map(int, input()))

# 첫 번째 스위치를 누르지 않는 경우
data1 = data[:]
result1 = try_solve(data1, n)

# 첫 번째 스위치를 누르는 경우
data2 = data[:]
switch(data2, 0, n)
result2 = try_solve(data2, n)

# 최소값 결정
if result1 != -1 and result2 != -1:
    final_result = min(result1, result2 + 1)
elif result1 != -1:
    final_result = result1
elif result2 != -1:
    final_result = result2 + 1
else:
    final_result = -1

print(final_result)