"""Giraffe"""
x = int(input())
y = []
count = 0
q = 0
for i in range(x):
    q = int(input())
    y.append(q)
if x == 1:
    print(1)
else:
    for i in range(x):
        if not i:
            if y[0] > y[1]:
                count += 1
        elif i == x-1:
            if y[i] > y[i-1]:
                count += 1
        else:
            if y[i] > y[i-1] and y[i] > y[i+1]:
                count += 1
    print(count)
