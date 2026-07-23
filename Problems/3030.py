"""saitama one punchhhhhhhhhhhh"""
import math as m
pushup = int(input())
situp = int(input())
upanddown = int(input())
run = int(input())
day_pushup = int(input())
day_situp = int(input())
day_run = int(input())
day_upanddown = int(input())

a = m.ceil(pushup / day_pushup)
b = m.ceil(situp / day_situp)
c = m.ceil(upanddown/day_upanddown)
d = m.ceil(run/day_run)
print(max(a,b,c,d))
