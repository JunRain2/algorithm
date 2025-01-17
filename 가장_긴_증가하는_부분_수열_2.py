n = int(input())

array = list(map(int, input().split()))


def max_permutations(array, index, cnt):
    if index >= n - 1:
        return cnt
    if array[index] < array[index + 1]:
        return max_permutations(array, index + 1, cnt + 1)
    elif array[index] > array[index + 1]:
        a = max_permutations(array, index + 1, cnt)
        b = max_permutations(array, index + 1, 1)
        return max(a, b)
    else:
        return max_permutations(array, index + 1, cnt)


print(max_permutations(array, 0, 1))
