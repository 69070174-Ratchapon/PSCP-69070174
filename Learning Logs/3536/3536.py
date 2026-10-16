"""isprimelarge"""
n = int(input())

if n < 2:
    print("NO")
elif n == 2:
    print("YES")
elif not n % 2:
    print("NO")
else:
    divisor = 3
    while divisor * divisor <= n:
        if not n % divisor:
            print("NO")
            break
        divisor += 2
    else:
        print("YES")
