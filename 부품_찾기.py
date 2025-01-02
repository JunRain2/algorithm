import sys

n = int(input())
n_array = list(map(int, sys.stdin.readline().rstrip().split()))[:n]
n_array.sort() 

m = int(input())
m_array = list(map(int, sys.stdin.readline().rstrip().split()))[:m]


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


result = list()
for i in m_array:
    r = "yes" if binary_search(n_array, i, 0, len(n_array) - 1) else "no"
    print(r, end=" ")
