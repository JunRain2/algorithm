n = int(input())

def calculate(a, b):
    if 9 * (10 ** (a)) < b:
        return (9 * (10 ** a)) * (a + 1) + calculate(a + 1, b - (9 * (10 ** a)))
    else:
        return b * (a + 1)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

print(calculate(0, n))