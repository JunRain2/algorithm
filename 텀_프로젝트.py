import sys
sys.setrecursionlimit(10**5)  # 재귀 깊이 제한 늘리기

def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = numbers[x]
    
    if visited[number]:
        if number in cycle:
            result += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n
    result = []
    
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    
    print(n - len(result))
