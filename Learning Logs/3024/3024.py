"""8urprise"""
x = float(input())
maximum = float(input())
minimum = x-(maximum*2)
if minimum < 0:
    minimum = 0
if maximum - minimum > 2:
    print("Surprising")
else:
    print("Not surprising")
