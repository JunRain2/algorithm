from itertools import combinations


# 정수, 입력한 정수를 담은 2차원 배열, 시스템 응답을 담은 1차원 배열
# 정수 n에서 서로 다른 5개의 수å
def solution(n, q, ans):
    answer = 0

    for comb in list(combinations(list(range(1, n + 1)), 5)):
        flag = True
        for i in range(len(ans)):
            if len(set(comb) & set(q[i])) != ans[i]:
                flag = False
                break
        if flag:
            answer += 1

    return answer
