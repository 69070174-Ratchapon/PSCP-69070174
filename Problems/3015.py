"""pro"""
x = int(input())
y = int(input())
a = int(input())
z = int(input())
r = z // x
c = z % x
if not c:
    print(y * a * r)
else :
    print(y * a * r + c * a)
