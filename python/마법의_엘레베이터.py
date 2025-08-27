def solution(storey):
    # 각 자릿수의 배열로 변경
    storey = list(map(int, reversed(str(storey)))) + [0]
    answer = 0

    for i in range(len(storey)):
        if storey[i] == 10:
            storey[i] = 0
            storey[i + 1] += 1

        if storey[i] == 5:
            if storey[i + 1] >= 5:
                storey[i + 1] += 1
            answer += 5
        elif storey[i] > 5:
            answer += 10 - storey[i]
            storey[i + 1] += 1
        else:
            answer += storey[i]
    return answer



def solution(storey):
    moves = 0
    
    while storey:
        digit = storey % 10
        storey //= 10
        
        if digit > 5 or (digit == 5 and storey % 10 >= 5):
            moves += 10 - digit
            storey += 1
        else:
            moves += digit
    
    return moves