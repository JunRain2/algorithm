def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, computers):
    answer = 0

    parent = list(range(n))

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and find_parent(parent, i) != find_parent(
                parent, j
            ):
                union_parent(parent, i, j)

    answer = len(set(parent))

    return answer
