from collections import deque

def can_transform(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

def solution(begin, target, words):
    n = len(words)
    words.append(begin)
    visited = [-1] * (n + 1)
    
    visited[n] = 0
    q = deque([n])
    while q:
        current = q.popleft()
        for i in range(n):
            if can_transform(words[current], words[i]) and visited[i] == -1:
                q.append(i)
                visited[i] = visited[current] + 1
                if words[i] == target:
                    return visited[i]

    return 0