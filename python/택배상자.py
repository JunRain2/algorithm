def solution(order):
    answer = 0
    order_index = 0
    stack = []
    
    for box in range(1, len(order) + 1):
        # 현재 박스를 스택에 넣음
        stack.append(box)
        
        # 스택의 탑이 필요한 박스와 일치하는 동안 계속 처리
        while stack and stack[-1] == order[order_index]:
            stack.pop()
            order_index += 1
            answer += 1
    
    return answer