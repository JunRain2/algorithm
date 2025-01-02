n, m = map(int, input().split())

array = list(map(int, input().split()))[:n]

value = max(array) - 1

while value > 0:
    a = list(filter(lambda x : x > value, array))
    result = sum(a) - (len(a) * value)
    
    if result >= m:
        print(value)
        break;
    else:
        value -= 1