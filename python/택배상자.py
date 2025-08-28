"""
1~n까지 순서대로 상자가 나옴
하지만 order의 순서대로 상자를 실어야 함

"""


def solution(order):
    answer = 0

    boxes = list(range(1, len(order)))

    order_index = 0
    stack = []

    # 1~n 까지의 박스가 순서대로 흘러들어간다.
    for i in range(1, len(order) + 1):
        # 현재 박스가 order에 맞지 않는다면
        if i != order[order_index]:
            if not stack:
                stack.append(i)
                continue

            # 보조 컨테이너에 마지막으로 들어간 값과 order가 맞는다면
            while stack and stack[-1] == order[order_index]:
                order_index += 1
                stack.pop()
                answer += 1

            stack.append(i)
        # 현재 박스가 order에 맞는다면
        else:
            order_index += 1
            answer += 1
            continue

    while stack and stack[-1] == order[order_index]:
        order_index += 1
        stack.pop()
        answer += 1

    return answer
