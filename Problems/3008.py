"""qwe"""
import math
a = float(input())
b = float(input())
c = float(input())
s = (a+b+c) / 2
q = math.sqrt(s * (s-a) * (s-b) * (s-c))
if a > 0 and b > 0 and c > 0:
    print(f"{q:.3f}")
