"""qwe"""
x1,y1,z1 = map(int,input().split())
x2,y2,z2 = map(int,input().split())
d = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
if isinstance(d,int):
    print(f"{d:.2f}")
else:
    print(f"{d:.2f}")
