from collections import Counter

r, c, k = map(int, input().split())
r -= 1
c -= 1
a = [list(map(int, input().split())) for _ in range(3)]


def row_sort(graph):
    result = []
    for line in graph:
        counter = Counter(line)
        counter.pop(0, None)  # 0은 빈 공간이므로 제외
        count_list = sorted(counter.items(), key=lambda x: (x[1], x[0]))
        tmp = []
        for num, cnt in count_list:
            tmp.append(num)
            tmp.append(cnt)
        result.append(tmp)
    for row in result:
        del row[100:]
    result = result[:100]
    max_len = max(len(row) for row in result)
    for row in result:
        row += [0] * (max_len - len(row))
    return result


def transpose(graph):
    x = len(graph)
    y = len(graph[0])
    return [[graph[i][j] for i in range(x)] for j in range(y)]


answer = -1
for i in range(101):
    x = len(a)
    y = len(a[0])

    if 0 <= r < x and 0 <= c < y and a[r][c] == k:
        answer = i
        break

    if x >= y:  # R 연산
        a = row_sort(a)
    else:       # C 연산
        a = transpose(row_sort(transpose(a)))

print(answer)