"""castle"""
x = int(input())
if x == 1:
    print("0")
elif x == 3:
    print("1")
elif x in (2,4):
    print("2")
elif x in (6,8):
    print("3")
elif x in (5,7,9):
    print("4")
elif x in (11,13,15):
    print("5")
elif x in (10,12,14,16):
    print("6")
elif x in (18,20,22,24):
    print("7")
elif x in (17,19,21,23,25):
    print("8")
