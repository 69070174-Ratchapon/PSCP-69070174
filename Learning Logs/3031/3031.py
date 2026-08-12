"""INK"""
import math
s,n = map(int,input().split())
result = 0
i = 0
while i < n:
    x,y = map(int,input().split())
    r = pow(x,2) + pow(y,2)
    result = 3.1416 * r/s
    print(math.ceil(result))
    i += 1
