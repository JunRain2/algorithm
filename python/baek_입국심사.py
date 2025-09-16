import heapq

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

q = []
for i in range(n):
    # 입국심사대가 끝났을 때를 기준으로 문제를 풀이
    # 종료 시간, 걸리는 시간
    q.append((arr[i], arr[i]))

result = 0
for _ in range(m):
    w, t = heapq.heappop(q)
    
    result = w
    w += t
    heapq.heappush(q, (w, t))
    
    
print(result)

"""
M명의 사람을 N개의 입국심사대에서 처리
"""