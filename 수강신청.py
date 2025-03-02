import sys
input = sys.stdin.readline

# 수강 가능 인원, 버튼을 클릭한 순서
k, l = map(int, input().split())
array = [input().strip() for _ in range(l)]

data = dict()
for i in array:
    if i in data:
        del data[i]
    data[i] = 0

data = list(data.keys())
for i in range(min(len(data), k)):
    print(data[i])