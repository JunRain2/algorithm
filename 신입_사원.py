for tc in range(int(input())):
    n = int(input())
    array = []
    for _ in range(n):
        a, b = map(int, input().split())
        array.append((a, b))
    array.sort()
    strd = array[0]
    result = 1
    for i in range(1, n):
        strd_a, strd_b = strd
        a, b = array[i]
        if strd_a > a or strd_b > b:
            result += 1
            strd = (a, b)
    print(result)