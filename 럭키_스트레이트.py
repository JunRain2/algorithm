n = input()

mid = int(len(n)/2)
first = map(int, n[:mid])
second = map(int, n[mid:])

if sum(first) == sum(second):
    print("LUCKY")
else:
    print("READY")
