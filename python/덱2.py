import sys
from collections import deque

def execute():
    input = sys.stdin.readline
    n = int(input())
    
    q = deque()
    for _ in range(n):
        inp = list(map(int, input().split()))
        if inp[0] == 1 or inp[0] == 2:
            perform(inp[0], q, inp[1])
        else:
            perform(inp[0], q)

def perform(command, q, x=-1):
    match command:
        case 1:
            q.appendleft(x)
        case 2:
            q.append(x)
        case 3:
            print(-1 if not q else q.popleft())
        case 4:
            print(-1 if not q else q.pop())
        case 5:
            print(len(q))
        case 6:
            print(0 if q else 1)
        case 7:
            print(-1 if not q else q[0])
        case 8:
            print(-1 if not q else q[-1])

execute()