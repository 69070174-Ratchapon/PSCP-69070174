"""password"""
name = input()
last_name = input()
age = int(input())
UPPER_CASE = str(age)
if len(name) >= 5 and len(last_name) >= 5:
    print(name[:2] + last_name[-1] + UPPER_CASE[-1])
else:
    print(name[0] + UPPER_CASE + last_name[-1])
