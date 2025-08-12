from collections import deque


# 게임별 이용자의 수, 서버 한 대로 감당할 수 있는 이용자 수, 서버 한 대가 운영 가능한 시간
def solution(players, m, k):
    answer = 0

    # 서버가 증설된 시간 + 5을 집어 넣음,
    q = deque()

    for i, player in enumerate(players):
        # peek를 반복적으로 확인하여 서버를 꺼내야할때까지 반복해서 꺼냄
        while q and q[0] == i:
            q.popleft()

        n = len(q)

        if (n + 1) * m <= player:
            p = (player - (n * m)) // m
            for _ in range(p):
                answer += 1
                q.append(i + k)
        print(len(q))

    return answer
