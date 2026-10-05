"""เกมสะสมแต้ม"""
num = int(input())
result = 0
q = ""
i = 0
while i < num:
    q = input()
    if q == "+":
        result += 10
    elif q == "-":
        result -= 5
    i += 1
print(result)
