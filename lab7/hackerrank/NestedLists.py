students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
scores = sorted(set([s[1] for s in students]))
second_lowest = scores[1]
names = sorted([s[0] for s in students if s[1] == second_lowest])
for n in names:
    print(n)