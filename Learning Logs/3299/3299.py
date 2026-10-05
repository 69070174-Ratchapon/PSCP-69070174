"แปลงดอกไม้"
L, N = map(int, input().split())

b = 1

while True:
    x = b * L
    p = x * (x + 1) // 2

    if p >= N:
        print(b)
        break

    b += 1
