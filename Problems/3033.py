"""gift"""
r,height,glue = map(float,input().split())
h = 2 * 3.14 * r + glue
w = (2 * r) + height
print(f"{w:.2f} {h:.2f}")
