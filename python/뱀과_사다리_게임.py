from collections import deque

n, m = map(int, input().split())

graph = [-1 for _ in range(101)]

jump = dict()

for _ in range(n + m):
    a, b = map(int, input().split())
    jump[a] = b
    
q = deque([1])
graph[1] = 0

while q:
    current = q.popleft()
    # 주사위를 굴림
    for i in range(1, 7):
        next = current + i
        if next <= 100:
            # 주사위를 굴린 곳에 사다리 or 뱀이 있는 경우 jump
            if next in jump.keys():
                next = jump[next]
            
            if next == 100:
                print(graph[current] + 1)
                exit()
            
            if graph[next] == -1:
                q.append(next)
                graph[next] = graph[current] + 1