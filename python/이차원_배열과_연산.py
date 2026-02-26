from collections import Counter

# r과 c는 1부터 시작함
r, c, k = map(int, input().split())
r -= 1
c -= 1
a = [list(map(int, input().split())) for _ in range(3)]


def row_sort(graph):
    result = []
    for line in graph:
        counter = Counter(line)
        count_list = sorted(counter.items(), key = lambda x: (x[1], x[0]))
        tmp = []
        for k, v in count_list:
            tmp.append(k)
            tmp.append(v)
        result.append(tmp)
    # 가장 긴 행 길이 찾기
    max_len = max(len(row) for row in result)
    # 짧은 행은 0으로 패딩
    for row in result:
        row += [0] * (max_len - len(row))

    return result


def turn_left(graph):
    x = len(graph)
    y = len(graph[0])

    tmp = [[0] * x for _ in range(y)]
    for i in range(x):
        for j, v in enumerate(sorted(graph[i])):
            tmp[j][i] = v

    return tmp

def turn_right(graph):
    x = len(graph)
    graph.reverse()

    tmp = [[0] * x for _ in range(y)]
    for i in range(x):
        for j, v in enumerate(graph[i]):
            tmp[j][i] = v

    return tmp

answer = -1
for i in range(100):
    x = len(a)
    y = len(a[0])

    # (r, c)의 좌표의 값이 k일 경우 해당 초를 기록하고 종료
    if 0 <= r < x and 0 <= c < y and a[r][c] == k:
        answer = i
        break

    if x >= y: # r연산을 실행
        a = row_sort(a)
    else: # c연산을 실행
        a = turn_right(row_sort(turn_left(a)))

        
print(answer)