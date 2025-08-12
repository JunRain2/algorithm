from collections import Counter

n = int(input())
s = list(input())
array = [list(input()) for _ in range(n-1)]

# 두개의 단어가 같은 종류의 문자로 이루어져 있다.
# 같은 문자는 같은 개수만큼 있다.

cnt_s = Counter(s)

result = 0
for c in array:
    cnt_c = Counter(c)
    cnt_w1 = cnt_c - cnt_s
    cnt_w2 = cnt_s - cnt_c
    
    diff_w1 = sum(cnt_w1.values())
    diff_w2 = sum(cnt_w2.values())
    
    if (diff_w1 == 1 and diff_w2 == 1) or diff_w1 + diff_w2 < 2:
        result += 1

    
# 단어의 차이가 무조건 2 미만이여야 하는거 아닌가?
# 바뀌는걸 고려해야함
print(result)