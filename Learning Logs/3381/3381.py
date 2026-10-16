"""pointsorting"""
x = int(input())
r = []

for _ in range(x):
    q = int(input())
    group = []
    for j in range(q):
        group.append(list(map(int,input().split())))
    r.append(group)
for group in r:
    group.sort(key=lambda point: (sum(point), point[0]))
for q in r:
    for j in q:
        print(*j)
