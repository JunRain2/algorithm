import heapq

solved_set = set()

def recommend(max_q, min_q, x):
    if x == 1:
        while max_q[0][1] in solved_set:  # -p가 저장되어 있으므로
            heapq.heappop(max_q)
        print(-max_q[0][1])
    elif x == -1:
        while min_q[0][1] in solved_set:
            heapq.heappop(min_q)
        print(min_q[0][1])

def add(max_q, min_q, p, l):
    heapq.heappush(max_q, (-l, -p))
    heapq.heappush(min_q, (l, p))

def solve(p):
    solved_set.add(p)

max_q, min_q = [], []
n = int(input())
for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(max_q, (-l, -p))
    heapq.heappush(min_q, (l, p))

m = int(input())
for _ in range(m):
    command = input().split()
    if command[0] == "recommend":
        recommend(max_q, min_q, int(command[1]))
    elif command[0] == "add":
        add(max_q, min_q, int(command[1]), int(command[2]))
    elif command[0] == "solved":
        solve(int(command[1]))
