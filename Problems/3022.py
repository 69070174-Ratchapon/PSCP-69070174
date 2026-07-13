"""temp"""
temp = float(input())
x = input().upper()
y = input().upper()
if x == "C" and y == "K":
    print(f"{temp + 273.15:.2f}")
elif x == "C" and y == "F":
    print(f"{temp * 9 / 5 + 32:.2f}")
elif x == "C" and y == "R":
    print(f"{(temp + 273.15) * 9 / 5:.2f}")
elif x == "K" and y == "C":
    print(f"{temp - 273.15:.2f}")
elif x == "K" and y == "F":
    print(f"{(temp - 273.15) * 9 / 5 + 32:.2f}")
elif x == "K" and y == "R":
    print(f"{temp * 9 / 5:.2f}")
elif x == "F" and y == "C":
    print(f"{(temp - 32) * 5 / 9:.2f}")
elif x == "F" and y == "K":
    print(f"{(temp - 32) * 5 / 9 + 273.15:.2f}")
elif x == "F" and y == "R":
    print(f"{temp + 459.67:.2f}")
elif x == "R" and y == "C":
    print(f"{temp * 5 / 9 - 273.15:.2f}")
elif x == "R" and y == "K":
    print(f"{temp * 5 / 9:.2f}")
elif x == "R" and y == "F":
    print(f"{temp - 459.67:.2f}")
elif x == y:
    print(f"{temp:.2f}")
