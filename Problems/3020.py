"""cocacola"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
remain = d - (b+1)
if b >= d:
    print(a * d)
elif not b:
    print(a * d)
elif b > 0:
    x = ((a * b) + c) + ((a * (b - 1) + c) * (remain // b)) + ((remain % b) * a)
    print(x)
