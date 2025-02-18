from collections import deque

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

def solution(n, costs):
    answer = 0
    parent = list(range(n))
    costs.sort(key = lambda x : x[2])
    
    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            answer += cost
            union_parent(parent, a, b)
    
    return answer