from collections import deque

# N명의 사람이 모두 제거될 때까지 계속
def execute():
    # 1번 부터 N번 까지의 사람, 순서대로 K 번째 사람을 제거
    n, k = map(int, input().split())
    
    q = deque(list(range(1, n + 1)))
    result = list()
    cnt = 1
    while q:
        v = q.popleft()
        if cnt == k:
            result.append(v)
            cnt = 1
        else:
            cnt = cnt + 1
            q.append(v)
    

    return output(result)

def output(result):
    return "<" + ", ".join(map(str, result)) + ">"

print(execute())
    