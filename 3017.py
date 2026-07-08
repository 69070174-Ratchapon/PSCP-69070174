"""bill"""
food = float(input())
q = food * 10/100
a = 0
if 50 <= q <= 1000:
    a = food + q
elif 0 < q < 50:
    a = food + 50
elif q >= 1000:
    a = food + 1000
a *= 1.07
print(f"{a:.2f}")
