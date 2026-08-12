"""castle"""
x = int(input())
count = 0
expo = 2
mod = 1
result = 1
if x == 1:
    print(0)
else:
    while count < 1:
        if pow(expo,2) >= x >= pow(expo,2) - (2 * (expo - 1)):
            if x % 2 == mod:
                print(result)
                count += 1
            else:
                print(result+1)
                count += 1
        result += 2
        expo += 1
        mod = (mod + 1) % 2
