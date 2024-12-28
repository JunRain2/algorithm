n, m = map(int, input().split())
card = list()

for _ in range(n):
    card.append(list(map(int, input().split()))[:m])

max = 0

for a in card:
    min_value = min(a)
    max = min_value if min_value > max else max

print(max)
