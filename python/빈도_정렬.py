"""
자주 등장하는 빈도 순으로 정렬
"""

n, c = map(int, input().split())
arr = list(map(int, input().split()))

counter = dict()
for i, value in enumerate(arr):
    if value not in counter.keys():
        counter[value] = [0, i]
    counter[value][0] -= 1

tmp = []
for key in counter.keys():
    tmp.append((*counter[key], key))
    
tmp.sort()
result = []
for cnt, _, value in tmp:
    result += [value] * (-cnt)

print(*result)