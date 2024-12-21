# 입력
score = int(
    input()
)  # input()은 문자형으로 입력을 받기 때문에 int()를 통해서 정수형으로 변경

# if문
if score >= 94:  # score를 정수형으로 변환하지 않으면 오류가 발생
    print("1등급")
elif score >= 87:
    print("2등급")
elif score >= 81:
    print("3등급")
else:
    print("3등급 미만")

# for 문
result = 0
for i in range(1, 51):  # range(닫힌구간, 열린구간)
    result += i

print(result)

name_list = ["홍길동", "이순신", "장보고"]

for i, element in enumerate(
    name_list
):  # enumerate()를 통해서 인덱스와 요소를 함께 가져올 수 있음
    print(i, element)  # 0 홍길동 1 이순신 2 장보고


# 함수
def add(a, b, c):
    return a + b + c


print(add(100, 200, 300))

# 자주 사용하는 라이브러리
data = [7, 2, 5, 4, 1]
print(sum(data))  # 배열을 모두 더함
print(min(data))  # 배열에서 가장 작은 값
print(max(data))  # 배열에서 가장 큰 값
print(sorted(data))  # 오름차순으로 정렬
print(sorted(data, reverse=True))  # 내림차순으로 정렬

# itertools : 순열, 조합, 중복 순열, 중복 조합 제공
from itertools import permutations  # 순열

arr = ["A", "B", "C"]
result = list(permutations(arr, 2))  # 순열
print(
    result
)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

from itertools import combinations  # 조합

result = list(combinations(arr, 2))
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

from itertools import product  # 중복 순열

result = list(product(arr, repeat=2)) # repeat : 중복을 포함해서 2개 선택하도록 
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

from itertools import combinations_with_replacement # 중복 조합

result = list(combinations_with_replacement(arr, 2))
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 우선순위 큐 목적으로 힙을 제공
import heapq # 최소 힙을 따름

arr = [5, 2, 9, 8, 7, 3, 4, 1, 6]
heap = []
result = []

for x in arr:
    heapq.heappush(heap, x)
    
for i in range(len(heap)):
    x = heapq.heappop(heap)
    result.append(x)
    
print(result) # [1, 2, 3, 4, 5, 6, 7, 8, 9] 오름차순과 같은 효과

# 입출력
# 5
# 35 92 89 54 22
n = int(input()) # 첫째 줄에는 학생의 수가 100 이하의 자연수
arr = list(map(int, input().split())) # 둘째 줄에는 각 할생의 저수가 100 이항의 양의 정수로 공백을 기준으로 구분


print(n)
print(arr)

# 입력 문자열이 다수의 문자열 -> 입력이 너무 많아 시간초과가 발생할 수 있음
import sys
input = sys.stdin.readline # 개행문자 \n까지 읽어들이므로, rstrip() 함수를 이용해 개행문자를 제거
data = input().rstrip()
print(data)

# f-string을 통해서 원하는 형태에 맞게 간단히 문자열을 출력
print(f"학생의 점수는 {score} 입니다.")
