"""calculator"""
n = int(input())
power_of = len(str(n)) - 1
count_one = 0
result = 0
if n == 1:
    print(1)
else:
    while count_one < len(str(n)):
        if not count_one:
            result += ((n + 1) - pow(10,power_of)) * len(str(n))
        else:
            result += ((pow(10,power_of + 1) - 1) - (pow(10,power_of)) + 1) * (power_of + 1)
        power_of -= 1
        count_one += 1
    result += n
    print(result)
