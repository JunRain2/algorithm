# 내장함수
# import 명령어 없이 사용 가능

print(
    eval("(3 + 5) * 7")
)  # 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환

result = sorted(
    [("홍길동", 35), ("이순신", 75), ("이무개", 50)], key=lambda x: x[1], reverse=True
)  # key 속성을 통해서 정렬 기준을 잡을 수 있음
print(result)

# 힙
# heapq외에 PriorityQueue가 존재하지만 heapq가 더 빠르게 동작하므로 heapq를 사용
import heapq


def min_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)  # heap.heappush()를 통해서 원소를 삽입
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))  # heapq.heappop()을 통해서 원소를 추출

    return result


result = min_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 파이썬에서는 최대 힙을 제공하지 않으므로 원소의 부호를 임시로 변경하는 방식을 사용
def max_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)  # heap.heappush()를 통해서 원소를 삽입
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))  # heapq.heappop()을 통해서 원소를 추출

    return result


result = max_heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# bisect
# 파이썬에서 이진 탐색을 쉽게 구현할 수 있도록 제공하는 라이브러리
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(
    bisect_left(a, x)
)  # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
print(
    bisect_right(a, x)
)  # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드


# bisect_left와 bisect_right는 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적으로 사용
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


print(count_by_range([1, 2, 3, 3, 3, 3, 4, 4, 8, 9], 4, 4))
print(count_by_range([1, 2, 3, 3, 3, 3, 4, 4, 8, 9], -1, 3))

# collections
# 유용한 자료구조를 제공하는 표준 라이브러리
"""
보통 파이썬에서는 dequeue를 이용해 큐를 구현
list는 append나 pop은 모두 맨 뒤 원소를 기준 -> 앞 쪽을 기준으로 할 때는 O(N)의 시간복잡도가 발생
하지만 dequeue는 모두 O(1)에 가능
인덱싱과 슬라이싱 등의 기능은 사용할 수 없다
스택이나 큐의 대용으로 사용할 수 있다.
"""
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)  # 첫 번째 인덱스에 원소 1을 삽입
data.append(5)  # 마지막 인덱스에 원소 5을 삽입

print(data)
print(list(data))  # 리스트 자료형으로 변환

print(data.popleft())  # 1 / 첫 번째 원소를 추출
print(data.pop())  # 5 / 마지막 원소를 추출

"""
Counter는 등장 횟수를 세는 기능을 제공
리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려줌
"""
from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"])  # 3
print(counter["red"])  # 2
print(dict(counter))  # 사전 자료형으로 변경 {'red': 2, 'blue': 3, 'green': 1}

# math
"""
자주 사용되는 수학적인 기능을 포함하고 있는 라이브러리
팩토리얼, 제곱근, 최대공약수 등을 계산해주는 기능을 포함
"""
import math

print(math.factorial(5))  # 5!를 반환 / 120
print(math.sqrt(7)) # 7의 제곱근을 출력 / 2.6457513110645907
print(math.gcd(21, 14)) # 21와 14의 최대 공약수를 출력 / 7
print(math.pi) # 파이 / 3.141592653589793
print(math.e) # 자연상수 e / 2.718281828459045