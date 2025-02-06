import heapq


def solution(jobs):
    answer = 0
    if not jobs:
        return 0

    jobs.sort(key=lambda x: x[0])
    current_time = 0
    job_queue = []
    job_index = 0

    while job_index < len(jobs) or job_queue:
        while job_index < len(jobs) and jobs[job_index][0] <= current_time:
            start_time, length = jobs[job_index]
            heapq.heappush(job_queue, (length, start_time))
            job_index += 1

        if job_queue:
            length, start_time = heapq.heappop(job_queue)
            current_time += length
            answer += current_time - start_time
        elif job_index < len(jobs):
            current_time = jobs[job_index][0]

    return answer // len(jobs)
