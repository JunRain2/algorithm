"""
visit는 queue를 활용
need_visit는 stack을 활용
1. 
"""
graph = {}

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

def dfs(graph, first_node):
    visited = []
    need_visit = []
    
    need_visit.append(first_node)
    
    while need_visit:
        node = need_visit.pop()
        
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited

print(dfs(graph, 'A')) # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']