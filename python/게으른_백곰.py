def execute() -> int:
    # 좌, 우 k만큼 떨어진 양동이까지 닿음
    n, k = map(int, input().split())
    positions = input_positions(n)

    # 엘버트가 택한 최적의 위치로부터 K만큼 떨어진 거리 내에 있는 얼음들의 합(최댓값)
    return max_ice(k, positions)


def input_positions(n):
    d = dict()

    for _ in range(n):
        g, x = map(int, input().split())
        d[x] = g

    return d


def max_ice(k, positions):
    arr = sum_ice(k, positions)

    return max(arr)


def sum_ice(k, positions):
    max_key = max(positions.keys())
    min_key = min(positions.keys())
    arr = [0] * (max_key + 1)

    for key in positions.keys():
        value = positions[key]
        arr[key] = arr[key] + value

        for i in range(1, k + 1):
            if (key - i) > min_key:
                arr[key - i] = arr[key - i] + value
            if (key + i) < max_key:
                arr[key + i] = arr[key + i] + value

    return arr

print(execute())