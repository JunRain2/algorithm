a = 0


def func():
    global a  # global 키워드를 통해서 함수 밖에있는 변수를 읽을 수 있음
    a += 1


for i in range(10):
    func()

print(a)


def add(a, b):
    return a + b


print(add(3, 7))  # 일반적인 함수 사용
print((lambda a, b: a + b)(3, 7))  # 람다 표현식으로 구현한 add() 메서드
