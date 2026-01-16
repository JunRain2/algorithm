from collections import deque


def execute():
    p = list(input())
    n = int(input())
    arr = input_arr()

    return output_arr(f_execute(p, arr))


def input_arr():
    data = input()
    data = data[1:-1]
    if not data:
        return list()

    return list(map(int, data.split(",")))


def output_arr(arr):
    if arr == "error":
        return arr
    
    return "[" + ",".join(map(str, arr)) + "]"


# 명령어에 맞춰 실행하는 메서드
def f_execute(p, a):
    arr = deque(a)
    # 정방향 True이면 앞에서, False이면 뒤에서 추출
    forward = True
    for f in p:
        if f == "D":
            if not arr:
                return "error"

            if forward:
                arr.popleft()
            else:
                arr.pop()

        if f == "R":
            forward = not forward

    # 정방향이면 그대로, 역방향이면 뒤집어서 반환
    return list(arr if forward else list(reversed(arr)))


for _ in range(int(input())):
    print(execute())

