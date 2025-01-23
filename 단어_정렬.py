n = int(input())
array = set()
for _ in range(n):
    array.add(input()) # set 자료형에서는 append()가 아닌 add()

array = list(array)
array.sort(key=lambda x : (len(x), x)) # 길이, 단어순
for i in array:
    print(i)