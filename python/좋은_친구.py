n, k = map(int, input().split())
ranks = [input() for _ in range(n)]

good_partner = 0
for left in range(n - 1):
    for right in range(left + 1, min(n, left + k + 1)):
        good_partner += 1 if len(ranks[left]) == len(ranks[right]) else 0
            
print(good_partner)