"""safepassword"""
char = input()
integer = input()
if char == "H" and integer == "4567":
    print("safe unlocked")
elif char == "H":
    print("safe locked - change digit")
elif integer == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
