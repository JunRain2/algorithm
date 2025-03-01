n, m = map(int, input().split())
# 단방향 그래프, 모든 노드를 거쳐야 함
edges = [tuple(map(int, input().split())) for _ in range(n)]
edges.sort()

result = m
r = (0, 0)
for a, b in edges:
    if a < b:
        continue
    if b <= r[0] <= a:
        if b <= r[1] <= a:
            continue
        result -= 2 * abs(r[0] - r[1])
        r = (a, r[1])
        result += 2 * abs(r[0] - r[1]) # 애매한 부분
    else:
        r = (a, b)
        result += 2 * abs(r[0] - r[1])


print(result)