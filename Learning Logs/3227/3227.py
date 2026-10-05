"""44"""
x = input().upper()
n = ""
symbol = ""
if len(x) == 3:
    n = x[:2]
    symbol = x[2]
elif len(x) == 2:
    n = x[0]
    symbol = x[1]
if n == "Q":
    if symbol == "D":
        print("queen of diamonds")
    elif symbol == "H":
        print("queen of hearts")
    elif symbol == "S":
        print("queen of spades")
    elif symbol == "C":
        print("queen of clubs")
elif n == "A":
    if symbol == "D":
        print("ace of diamonds")
    elif symbol == "H":
        print("ace of hearts")
    elif symbol == "S":
        print("ace of spades")
    elif symbol == "C":
        print("ace of clubs")
elif n == "J":
    if symbol == "D":
        print("jack of diamonds")
    elif symbol == "H":
        print("jack of hearts")
    elif symbol == "S":
        print("jack of spades")
    elif symbol == "C":
        print("jack of clubs")
elif n == "K":
    if symbol == "D":
        print("king of diamonds")
    elif symbol == "H":
        print("king of hearts")
    elif symbol == "S":
        print("king of spades")
    elif symbol == "C":
        print("king of clubs")
else:
    if symbol == "D":
        print(f"{n} of diamonds")
    elif symbol == "H":
        print(f"{n} of hearts")
    elif symbol == "S":
        print(f"{n} of spades")
    elif symbol == "C":
        print(f"{n} of clubs")
