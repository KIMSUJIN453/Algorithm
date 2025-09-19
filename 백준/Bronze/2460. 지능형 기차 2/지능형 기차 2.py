max_people = 0
people = 0

for i in range(10):
    OUT, IN = map(int, input().split())
    people -= OUT
    people += IN
    if people > max_people:
        max_people = people

print(max_people)