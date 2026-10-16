"""Duplicate"""
list_a = []
list_b = []
result = []
a = int(input())
b = int(input())
for i in range(a):
    list_a.append(int(input()))
for i in range(b):
    list_b.append(int(input()))
for i in list_a:
    for j in list_b:
        if i == j:
            result.append(i)
            break
result.sort()
if not result:
    print("Nope")
else:
    for i in result[::-1]:
        print(i)
