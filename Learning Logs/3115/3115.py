"""Storecheck"""
n,check1 = map(int,input().split())

q = []
result = 0
total = ""
check = []
if check1 or not check1:
    for i in range(n):
        opens,close = map(int,input().split())
        q.append([opens,close])
    check = input().split()

for i in check:
    for opens,close in q:
        if opens <= int(i) < close:
            result += 1
    total += str(result) + " "
    result = 0
print(total.strip())
