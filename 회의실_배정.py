n = int(input())

array = []

for _ in range(n):
    array.append(tuple(map(int, input().split())))  # 시작시간, 끝나는시간

array.sort(key=lambda x: (x[1], x[0]))

start, end = array[0]
result = 1
for i in range(1, n):
    tmp_start, tmp_end = array[i]
    if end <= tmp_start:
        result += 1
        start, end = tmp_start, tmp_end

print(result)
