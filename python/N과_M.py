from itertools import permutations

n, m = map(int, input().split())

result = sorted(permutations(range(1, n + 1), m))

for i in result:
    print(*i)