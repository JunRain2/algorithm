# 카드 N개가 포함된 N가지 카드팩
# 돈을 많이 써서 N개의 카드팩을 구매
n = int(input())
array = [0] + list(map(int, input().split()))
dp = dict()


# 백트래킹 연산
def dfs(pay, card):
    if card == n:
        return pay
    if (pay, card) in dp.keys():
        return dp[(pay, card)]
    dfs_result = []
    for i in range(1, n + 1):
        if card + i > n:
            continue
        dfs_result.append(dfs(pay + array[i], card + i))
    dp[(pay, card)] = max(dfs_result)

    return dp[(pay, card)]


print(dfs(0, 0))
