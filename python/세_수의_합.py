n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

possible_sums = set()
answer = None

for i in range(n):
    # arr[i]가 세 수의 합으로 표현 가능한지 확인
    for j in range(i):
        if arr[i] - arr[j] in possible_sums:
            answer = arr[i]
    # 다음 인덱스를 위해 현재 i까지의 모든 쌍 합을 추가
    for j in range(i+1):
        possible_sums.add(arr[i] + arr[j])

print(answer)
