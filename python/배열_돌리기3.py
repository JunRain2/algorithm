n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def td(arr):
    result = []
    for i in range(n - 1, -1, -1):
        result.append(arr[i])
    return result


def lr(arr):
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = arr[i][(m - 1) - j]

    return result


def tr(arr):
    global n, m
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = arr[i][j]
    
    n, m = m, n
    return result


def tl(arr):
    global n, m
    result= [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - 1 - j][i] = arr[i][j]
    
    n, m = m, n
    return result

def device(arr):
    one = []
    two = []
    three = []
    four =[]
    
    for i in range(n):
        if 0 <= i < n/2:
            one.append(arr[i][:m//2:])
            two.append(arr[i][m//2::])
        else:
            four.append(arr[i][:m//2:])
            three.append(arr[i][m//2::])            
    
    return one, two, three, four

def combine(one, two, three, four):
    result = []
    
    for i in range(n//2):
        result.append(one[i] + two[i])
    
    for i in range(n//2):
        result.append(four[i] + three[i])
        
    return result
    

def five(arr):
    one, two, three, four = device(arr)
    
    return combine(four, one, two, three)

def six(arr):
    one, two, three, four = device(arr)
    
    return combine(two, three, four, one)


orders = list(map(int, input().split()))

for order in orders:
    if order == 1:
        arr = td(arr)
    elif order == 2:
        arr = lr(arr)
    elif order == 3:
        arr = tr(arr)
    elif order ==  4:
        arr = tl(arr)
    elif order == 5:
        arr = five(arr)
    elif order == 6:
        arr = six(arr)

for row in arr:
    print(*row)
