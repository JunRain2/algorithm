from collections import Counter

s, p = map(int, input().split())
data = list(input())
cnt = list(map(int, input().split()))

counter = Counter(data[0:p])

def check(counter):
    return (
        counter["A"] >= cnt[0]
        and counter["C"] >= cnt[1]
        and counter["G"] >= cnt[2]
        and counter["T"] >= cnt[3]
    )


result = 0 + check(counter)
i = 0
while p + i < s:
    counter[data[i]] -= 1
    counter[data[i + p]] += 1
    result += check(counter)

    i += 1

print(result)
