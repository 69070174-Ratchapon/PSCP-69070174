"""BRICKS"""
import math as m
a = int(input())
b = int(input())
goal = int(input())
q = goal - (b * 5)
if q < 0:
    remain = q + (5 * (abs(m.ceil(q / 5)) + 1))
    if a >= remain:
        print(remain)
    else:
        print(-1)
else:
    if a >= q:
        print(q)
    else:
        print(-1)
