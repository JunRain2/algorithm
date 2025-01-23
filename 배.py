n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

if max(cranes) < max(boxes):
    print(-1)
    exit()

# 크레인, 박스 모두 내림차순 정렬
cranes.sort(reverse=True)
boxes.sort(reverse=True)

result = 0
# 모든 박스가 옮겨질 때까지 반복
while boxes:
    for crane in cranes:
        # 현재 크레인으로 옮길 수 있는 가장 무거운 박스를 찾으면 바로 제거
        for i in range(len(boxes)):
            if boxes[i] <= crane:
                boxes.pop(i)
                break
    result += 1
    
print(result)