"""num"""
num = int(input())
op = input()
REVERSE_NUM = int(str(num)[::-1])
if op == "*":
    print(f"{num} * {REVERSE_NUM} = {num * REVERSE_NUM}")
elif op == "+":
    print(f"{num} + {REVERSE_NUM} = {num + REVERSE_NUM}")
