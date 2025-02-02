def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    
    return answer.join(numbers)