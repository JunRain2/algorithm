from collections import Counter

# 입력 받기
name = input().strip()

# 각 문자의 등장 횟수 세기
count = Counter(name)

# 홀수 개수인 문자 찾기
odd = 0
odd_char = ''
for char, freq in count.items():
    if freq % 2 == 1:
        odd += 1
        odd_char = char

# 팰린드롬 불가능한 경우
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    # 팰린드롬 만들기
    result = ''
    # 사전순으로 앞쪽 절반 만들기
    for char in sorted(count.keys()):
        result += char * (count[char] // 2)
    
    # 중간에 홀수 문자 넣기
    answer = result + odd_char + result[::-1]
    print(answer)
