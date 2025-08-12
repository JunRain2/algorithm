from collections import Counter

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

# 산술평균
def get_mean():
    return round(sum(numbers) / n)

# 중앙값
def get_median():
    numbers.sort()
    return numbers[n//2]

# 최빈값
def get_mode():
    count = Counter(numbers)
    modes = count.most_common()
    if len(numbers) > 1:
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
    return modes[0][0]

# 범위
def get_range():
    return max(numbers) - min(numbers)

print(get_mean())
print(get_median())
print(get_mode())
print(get_range())
