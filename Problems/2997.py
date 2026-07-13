"""ELO"""
ra = int(input())
rb = int(input())
q = input()
ea = 1 / (1 + (10 ** ((rb - ra)/400)))
eb = 1 / (1 + (10 ** ((ra - rb)/400)))
if ra >= 0 and rb >= 0:
    if q == "A":
        print(f"{ea:.2f}")
    elif q == "B":
        print(f"{eb:.2f}")
