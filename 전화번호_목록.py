def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort() # 길이가 작은 수부터
    
    for i in range(n):
        for j in range(i + 1, n):
            if phone_book[j].startswith(phone_book[i]):
                return False
            
    return answer