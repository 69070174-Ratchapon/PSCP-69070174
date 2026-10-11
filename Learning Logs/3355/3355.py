"""zxc"""
result = []
start = None
end = None

while True:
    number = int(input())

    if number == -1:
        break

    if start is None:
        start = end = number
    elif number == end + 1:
        end = number
    else:
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}-{end}")

        start = end = number

if start is not None:
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")
print(", ".join(result))
