""" 
visited_queue : 방문한 큐
need_visit queue : 방문할 큐
1. 방문한 큐에 방문한 노드를 삽입 -> 방문할 큐에 방문한 노드와 연결된 노드를 모두 삽입
2. 방문할 큐에서 노드를 꺼내 1번을 반복
"""

graph = {}  # 그래프를 딕셔너리로 구성

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]


def bfs(graph, start_node):
    visited = []  # 라이브러리 Queue를 활용할 수 있지만, 기본 list에서도 가능
    need_visit = []

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(
            0
        )  # pop(index) index에 있는 값을 뺄 수 있음, 라이브러리가 알아서 값을 채워넣음

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])  # extend()를 통해서 list를 합쳐줄 수 있음

    return visited


print(bfs(graph, "A"))  # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
