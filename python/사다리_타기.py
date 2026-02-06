k = int(input()) # 참가자 수, 열
n = int(input()) # 가로 수, 행

results = list(input()) # 최종 순서
graph = [list(input()) for _ in range(n)]

players = [chr(i) for i in range(ord('A'), ord('A') + k)]

def top_down(curr):
    current = curr
    
    for i in range(n):
        if ['?'] * (k - 1) == graph[i]:
            return current
        
        tmp = [''] * k
        
        for j in range(k):
            # 오른쪽으로 갈 수 있을 때
            if j < k - 1 and graph[i][j] == '-':
                tmp[j + 1] = current[j]
            # 왼쪽으로 갈 수 있을 때
            elif j > 0 and graph[i][j - 1] == '-':
                tmp[j - 1] = current[j]
            # 그냥 올라가야 할 때
            else:
                tmp[j] = current[j]
            
        current = tmp
        
        
def bottom_up(curr):
    current = curr
    
    for i in range(n - 1, -1, -1):
        if ['?'] * (k - 1) == graph[i]:
            return current
        
        tmp = [''] * k
        
        for j in range(k):
            # 오른쪽으로 갈 수 있을 때
            if j < k - 1 and graph[i][j] == '-':
                tmp[j + 1] = current[j]
            # 왼쪽으로 갈 수 있을 때
            elif j > 0 and graph[i][j - 1] == '-':
                tmp[j - 1] = current[j]
            # 그냥 올라가야 할 때
            else:
                tmp[j] = current[j]
            
        current = tmp

top = top_down(players)
bottom = bottom_up(results)

result = []

for i in range(k - 1):
    if top[i] == bottom[i]:
        result.append('*')
    elif i < k - 1 and top[i] == bottom[i + 1]:
        result.append('-')
        bottom[i], bottom[i + 1] = bottom[i + 1], bottom[i]
    else:
        result = None
        break

print(('x'*(k-1)) if result == None else "".join(result))