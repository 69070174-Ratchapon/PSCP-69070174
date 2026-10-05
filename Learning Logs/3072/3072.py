"""AEIOU"""
letter = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for j in letter:
    if j == "a":
        a += 1
    elif j == "e":
        e += 1
    elif j == "i":
        i += 1
    elif j == "o":
        o += 1
    elif j == "u":
        u += 1
if a > 0:
    print(f"a : {a}")
if e > 0:
    print(f"e : {e}")
if i > 0:
    print(f"i : {i}")
if o > 0:
    print(f"o : {o}")
if u > 0:
    print(f"u : {u}")
