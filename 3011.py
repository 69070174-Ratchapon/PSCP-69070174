"""color"""
colour_1 = input().upper()
colour_2 = input().upper()
if (colour_1 == "RED" and colour_2 == "YELLOW"):
    print("Orange")
elif (colour_2 == "RED" and colour_1 == "YELLOW"):
    print("Orange")
elif (colour_1 == "RED" and colour_2 == "BLUE"):
    print("Violet")
elif (colour_2 == "RED" and colour_1 == "BLUE"):
    print("Violet")
elif (colour_1 == "YELLOW" and colour_2 == "BLUE"):
    print("Green")
elif (colour_2 == "YELLOW" and colour_1 == "BLUE"):
    print("Green")
elif (colour_1 == "RED" and colour_2 == "RED") or (colour_2 == "RED" and colour_1 == "RED"):
    print("Red")
elif (colour_1 == "BLUE" and colour_2 == "BLUE") or (colour_2 == "BLUE" and colour_1 == "BLUE"):
    print("Blue")
elif (colour_1 =="YELLOW" and colour_2 == "YELLOW") or \
    (colour_2 == "YELLOW" and colour_1== "YELLOW"):
    print("Yellow")
else:
    print("Error")
