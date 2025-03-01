for tc in range(int(input())):
    n, m = map(int, input().split())
    data = [tuple(map(int, input().split())) for _ in range(m)]
    data.sort(key=lambda x: (x[1], x[0]))  # 끝번호(b), 시작번호(a) 순으로 정렬

    visited = [False] * (n + 1)  # 각 책 번호의 배정 여부를 기록
    answer = 0

    for a, b in data:
        for book in range(a, b + 1):  # 학생이 원하는 범위 내에서
            if not visited[book]:  # 아직 배정되지 않은 책이 있다면
                visited[book] = True  # 해당 책을 배정
                answer += 1
                break

    print(answer)
