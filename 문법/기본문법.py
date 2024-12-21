# 문자열 슬라이싱
a = "Hello World"

prefix = a[:4]  # 0~3까지 -> 열린 구간
print(prefix)
suffix = a[2:]  # 2~ 까지 -> 닫힌 구간
print(suffix)

print(a[:50])  # 인덱스 범위를 초과 -> 오류를 발생시키지 않고 마지막 인덱스를 가져옴

# 리스트 -> 가변객체
data = ["Hell", 7, 0.5]  # 서로 다른 자료형 가능

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a + b)  # 리스트의 더하기 가능

# 2차원 이상의 리스트를 초기화할 떄는 리스트 컴프리헨션(list comprehension)을 사용
# [{실행문} for {변수} in range({num})] // for문의 조건만큼 실행문을 실행
arr = [5] * 8  # 원소를 8개 포함하는 1차원 리스트
print(arr)  # [5, 5, 5, 5, 5, 5, 5, 5]

arr = [
    [0] * 5 for _ in range(4)
]  # 4 * 5 크기를 갖는 2차원 리스트, _ : 임시변수 혹은 throwaway로 파이썬의 특별한 관례
print(arr)  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

arr = [[i] * 5 for i in range(4)]  # 4 * 5 크기를 갖는 2차원 리스트
print(arr)  # [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3]]

arr = [
    [(i * 5) + j for j in range(5)] for i in range(4)
]  # 4 * 5 크기를 갖는 2차원 리스트
print(
    arr
)  # [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]

# 사전(Dictionary) 자료형 -> Java의 Map
# key value 형태
data = {}  # 초기화
data["apple"] = "사과"
data["banana"] = "바나나"

for key in data.keys():  # keys()를 통해서 모든 키를 확인
    print("key:", key, "value", data[key])

data = [1, 3, 3, 5, 4, 3, 1, 4]
counter = {}

for x in data:  # data 의 숫자들을 카운팅 -> 자주 사용
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1
print(counter)  # {1: 2, 3: 3, 5: 1, 4: 2}

# 집합(Set) 자료형
# 특정한 데이터가 등장한 적 있는지 체크할 때 효과적으로 사용
data = [1, 3, 3, 5, 4, 3, 1, 4]
visited = set()

for x in data:
    if x not in visited:
        visited.add(x)
    else:
        print("중복 원소 발견 :", x)
print("고유한 원소들", visited)
