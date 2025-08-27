"""
100 장, 1 ~ 100 까지 숫자 하나씩
[2, 100] 하나 정해 그 수보다 작거나 같은 숫자를 준비, 준비된 숫자 수만큼 작은 상자를 준비하면 게임을 시작할 수 있다.

준비된 상자에 카드를 한 장씩, 상자를 무작위로 섞어 나열

임의의 상자를 하나 선택하여 선택한 상자 안의 숫자 카드를 확인
확인한 카드에 적힌 번호에 해당하는 상자를 열어 안에 담긴 카드에 적힌 숫자를 확인 (3을 뽑으면 3번 상자를 연다)
상자가 이미 열려있을때까지 반복

1번 상자 그룹에 속한 상자의 수와 2번 상자 그룹에 속한 상자의 수를 곱한 값이 게임의 점수
"""


def solution(cards):
    answer = 0
    # 1~n까지
    groups = []

    cards = [0] + cards
    n = len(cards)
    visited = [False] * (n + 1)

    def game(index):
        cnt = 1
        visited[index] = True
        while True:
            index = cards[index]
            if visited[index]:
                break
            visited[index] = True
            cnt += 1
        return cnt

    for i in range(1, n):
        if visited[i]:
            continue
        groups.append(game(i))

    groups = list(reversed(sorted(groups)))

    return 0 if len(groups) <= 1 else groups[0] * groups[1]
