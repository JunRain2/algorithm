# 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깍이게 된다.
# 내구도가 0이되는 순간 계란은 깨지게 된다.
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

# 1. 가장 왼쪽의 계란을 든다.
# 2. 깨지지 않은 계란 중 하나를 침
# 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘아감
# 손에 든 계란을 원래 자리에 내려놓고 3번 진행
# 3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정 진행
# 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 종료


def broken_eggs(eggs):
    cnt = 0
    for s, _ in eggs:
        if s <= 0:
            cnt += 1

    return cnt


def back_tracking(eggs, cur):
    # 맨 오른쪽인 경우
    if cur == n:
        return broken_eggs(eggs)

    # 손에 있는 계란이 깨진 경우
    if eggs[cur][0] <= 0 or broken_eggs(eggs) >= n - 1:
        return back_tracking(eggs, cur + 1)

    result = 0
    for i in range(n):
        # 깨진 계란인 경우 pass
        if i == cur or eggs[i][0] <= 0:
            continue

        eggs[cur][0] -= eggs[i][1]
        eggs[i][0] -= eggs[cur][1]

        result = max(result, back_tracking(eggs, cur + 1))

        eggs[cur][0] += eggs[i][1]
        eggs[i][0] += eggs[cur][1]

    return result


print(back_tracking(eggs, 0))
