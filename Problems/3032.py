"""saitama"""
x = int(input())
i = 0
a = 0
for i in range(x):
    q = int(input())
    if not i:
        high = q
        a += 1
    elif q == high:
        a += 1
    elif q > high:
        high = q
        a = 1
print(high)
print(a)
