# N(가게의 부품 개수)을 입력받기
n = int(input())
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수)을 입력 받기
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input()).split())

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = "yes" if i in array else "no"
    print(result, end=" ")
