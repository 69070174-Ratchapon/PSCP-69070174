"""lottery"""
x1,x2 = input().split()
y1,y2 = input().split()
if x1 == y1 and x2 == y2:
    print(1000000)
elif x2 == y2:
    print(100000)
elif x2[-3:] == y2[-3:] and x1 == y1:
    print(2000)
elif x2[-2:] == y2[-2:] and x1 == y1:
    print(1000)
elif x2[-3:] == y2[-3:]:
    print(200)
elif x2[-2:] == y2[-2:]:
    print(100)
elif x1 == y1:
    print(20)
else:
    print(0)
