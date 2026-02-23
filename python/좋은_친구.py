from collections import deque, defaultdict

n, k = map(int, input().split())
ranks = [input() for _ in range(n)]

queues = defaultdict(deque)
answer = 0

for i in range(n):
    length = len(ranks[i])
    
    while queues[length] and i - queues[length][0] > k:
        queues[length].popleft()
    
    answer += len(queues[length])
    queues[length].append(i)

print(answer)