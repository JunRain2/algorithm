n = int(input())

array = []

for _ in range(n):
    array.append(tuple(map(int, input().split())))  # 시작시간, 끝나는시간

array.sort(key=lambda x: (x[0], x[1]))

result = 1
start, end = array[1]
for i in range(1, n):
    tmp_start, tmp_end = array[i]
    if tmp_end < end:  # cost가 더 적을 경우
        start, end = tmp_start, tmp_end
    elif end <= tmp_start:
        start, end = tmp_start, tmp_end
        result += 1
    else:
        continue

print(result)
