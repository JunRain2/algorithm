n = int(input())
tops = list(map(int, input().split()))

buildings = dict()

# 정방향 순회, i 기준으로 왼쪽에 머가 보이는지 
stack = []
for i in range(n):
    if not stack:
        stack.append((tops[i],i))
        continue
    
    
    prev = tops[i]
    while stack and stack[-1][0] <= prev:
        stack.pop()
        
    if stack:
        # 거리, 인덱스 번호
        near = stack[-1][1]
        buildings[i] = (near ,len(stack))
        
    stack.append((tops[i], i))
    
# 역방향 순회, i 기준으로 오른쪽에 머가 보이는지
stack = [] # distance, num
for i in range(n-1, -1, -1):
    if not stack:
        stack.append((tops[i],i))
        continue
    
    
    prev = tops[i]
    while stack and stack[-1][0] <= prev:
        stack.pop()
    
    if stack:
        # 거리, 인덱스 번호
        near = stack[-1][1]
        if i not in buildings:
            buildings[i] = (near ,len(stack))      
        else: 
            left_distance = abs(i - buildings[i][0])
            right_distance = abs(i - near)
            buildings[i]= (buildings[i][0] if left_distance <= right_distance else near, buildings[i][1] + len(stack))
            
    stack.append((tops[i], i))

for i in range(n):
    if i not in buildings:
        print(0)
    else:
        print(buildings[i][1], buildings[i][0] + 1)