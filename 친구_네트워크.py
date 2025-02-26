def find(x, parent):
    # x의 루트를 찾고 경로 압축 수행
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, size):
    # 각 노드의 루트를 찾음
    root_x = find(x, parent)
    root_y = find(y, parent)

    # 이미 같은 네트워크이면 해당 네트워크의 크기를 반환
    if root_x == root_y:
        return size[root_x]

    # 크기가 작은 트리를 큰 트리 밑으로 붙임 (Union by Size)
    if size[root_x] < size[root_y]:
        root_x, root_y = root_y, root_x
        
    parent[root_y] = root_x
    size[root_x] += size[root_y]
    return size[root_x]


T = int(input())
for _ in range(T):
    f = int(input())
    # 각 친구의 부모와 네트워크 크기를 저장할 딕셔너리
    parent = dict()
    size = dict()

    for _ in range(f):
        a, b = input().split()
        
        # 친구가 처음 등장하면 초기화 (자기 자신을 부모로, 크기 1)
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
        
        # 두 친구를 합치고, 결과 네트워크의 크기를 출력
        network_size = union(a, b, parent, size)
        print(network_size)