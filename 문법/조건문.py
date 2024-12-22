# 파이썬의 논리 연산자는 and, or, not을 사용
# 자바나 다른 언어처럼 &&, ||, !을 사용하지 않는다.

score = 85
result = "Success" if score >= 80 else "Fail"  # 조건부 표현식 -> 3항 연산자와 같은 역할

x = 15
if x > 0 and x < 20: # 다른 문법과 헷갈리지 않게 
    print("x는 0이상 20 미만의 수")
if 0 < x < 20:
    print("x는 0이상 20 미만의 수")
