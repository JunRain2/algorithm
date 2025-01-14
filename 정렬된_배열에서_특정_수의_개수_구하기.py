# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == -1:
        return 0  # 값이 x인 원소의 개수는 0개이므로 0 반환

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return b - a + 1


# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid
            end = mid - 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result


def last(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result = mid
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)