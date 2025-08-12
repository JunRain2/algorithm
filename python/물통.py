from collections import deque

a, b, c = map(int, input().split())
capacity = [a, b, c]

q = deque()
q.append((0, 0, c))
visited = set()
visited.add((0, 0, c))
result = set()

while q:
    state = q.popleft()
    A, B, C = state

    if A == 0:
        result.add(C)

    bottles = [A, B, C]

    for from_idx in range(3):
        for to_idx in range(3):
            if from_idx == to_idx:
                continue

            new = bottles[:]
            # 이동 가능한 양 = min(보내는 물의 양, 받는 쪽의 남은 용량)
            amount = min(new[from_idx], capacity[to_idx] - new[to_idx])
            if amount == 0:
                continue

            new[from_idx] -= amount
            new[to_idx] += amount
            new_state = tuple(new)

            if new_state not in visited:
                visited.add(new_state)
                q.append(new_state)

print(*sorted(result))