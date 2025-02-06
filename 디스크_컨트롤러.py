import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    q = []
    current_time = 0
    idx = 0
    while True:
        if idx >= len(jobs):
            break
        # 현재 스케줄러가 끝났을 때, 시간보다 작으면 큐에 입력
        if current_time >= jobs[idx][0]:
            s, l = jobs[idx]
            heapq.heappush(q, (l, s, idx))
            idx += 1
        # 현재 스케줄러가 끝났을 때, 시간보다 크면
        else:
            while q:
                l, s, i = heapq.heappop(q)
                current_time += l
                answer += current_time - s
            s, l = jobs[idx]
            heapq.heappush(q, (l, s, idx))
            idx += 1

    # jobs의 값을 모두 q에 넣었을 경우 털어줘야 함
    while q:
        l, s, i = heapq.heappop(q)
        current_time += l
        answer += current_time - s

    return answer // len(jobs)
