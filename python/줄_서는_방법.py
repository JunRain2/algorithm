def solution(n, k):
    import math

    people = list(range(1, n + 1))
    answer = []
    k -= 1  # 0-based

    for i in range(n):
        factorial = math.factorial(n - 1 - i)
        index = k // factorial

        answer.append(people[index])
        people.remove(people[index])  # 또는 del people[index]

        k %= factorial

    return answer
