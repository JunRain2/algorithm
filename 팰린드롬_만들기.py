from collections import Counter

array = list(input())
if len(array) <= 1:
    print("I'm Sorry Hansoo")
    exit()
counter = Counter(array)
array_counter = list(counter.most_common())
array_counter.sort()

result = []
odd_word = ""
if len(array) % 2 == 0:  # 짝수 일 떄
    for word, cnt in array_counter:
        if cnt % 2 != 0:
            print("I'm Sorry Hansoo")
            exit()
        for _ in range((cnt // 2)):
            result.append(word)
else:  # 홀수 일 떄
    odd = 0
    for word, cnt in array_counter:
        if cnt % 2 != 0:
            if odd > 0:
                print("I'm Sorry Hansoo")
                exit()
            else:
                odd_word = word
                odd += 1
        for _ in range((cnt // 2)):
            result.append(word)

print("".join(result) + "".join(odd_word) + "".join(result[::-1]))
