from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

temp = []         # 각 길이의 증가 부분 수열의 마지막 원소를 저장
indices = []      # temp의 각 원소가 실제 arr에서 어디 인덱스를 가리키는지
parent = [-1] * n # LIS를 복원하기 위한 부모 인덱스 정보

for i in range(n):
    # arr[i]가 들어갈 위치(길이)를 찾음
    pos = bisect_left(temp, arr[i])

    # temp의 길이를 넘어서면 새 원소로 확장
    if pos == len(temp):
        temp.append(arr[i])
        indices.append(i)
    # 기존 위치를 갱신
    else:
        temp[pos] = arr[i]
        indices[pos] = i

    # pos가 0보다 크다면, 바로 앞 길이의 마지막 원소가 parent가 됨
    if pos > 0:
        parent[i] = indices[pos - 1]

# LIS 길이
length = len(temp)

# 실제 LIS 복원
lis = []
idx = indices[-1] # 가장 긴 길이의 마지막 원소의 인덱스
while idx != -1:
    lis.append(arr[idx])
    idx = parent[idx]
lis.reverse()

print(length)
print(*lis)
