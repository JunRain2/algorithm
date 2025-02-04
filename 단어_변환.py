from collections import deque

def solution(begin, target, words):
    n = len(words)
    words.append(begin)
    visited = [-1] * (n + 1)
    
    visited[n] = 0
    q = deque([n])
    while q:
        current = q.popleft()
        for i in range(n):
            t = set(list(words[i])) & set(list(words[current]))
            if len(t) == len(words[current]) - 1 and visited[i] == -1:
                q.append(i)
                visited[i] = visited[current] + 1
                if words[i] == target:
                    return visited[i]

    return 0