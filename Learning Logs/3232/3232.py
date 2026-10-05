"""กบน้อยกระโดด"""
x,y = map(int,input().split())
a = 0
count = 0
while a < y and x > 0:
    a += x
    x -= 2
    count += 1
if a < y:
    print(-1)
else:
    print(count)
