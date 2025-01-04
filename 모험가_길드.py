n = int(input())
people = list(map(int, input().split()))[:n]

people.sort(reverse=True)

group = 0

while people:
    person = people[0]
    if person > len(people):
        break

    group += 1
    people = people[person:]

print(group)
