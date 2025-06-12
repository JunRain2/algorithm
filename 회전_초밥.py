# 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우, 할인된 정액 가격 제공
# 손님이 먹을 수 있는 초밥 가짓수의 최댓값

# 접시의 수, 초밥의 가짓 수, 연속해서 먹는 접시의 수, 쿠폰 번호 c
n, d, k, c = map(int, input().split())
graph = [int(input()) for _ in range(n)]
graph += graph

left, right = 0, k

result = 0
for i in range(n + 1):
    if right >= (2 * n):
        break

    s = set(graph[left:right])
    cnt = len(s) + (1 if c not in s else 0)
    result = max(result, cnt)

    left += 1
    right += 1

print(result)
