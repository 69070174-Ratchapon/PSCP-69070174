"""flashexpress"""
start,end = map(str,input().split())
weight = float(input())
if start == "BKK" and end == "CNX":
    print(f"{10 + 30 * weight:.2f}")
elif start == "CNX" and end == "UBP":
    print(f"{15 + 40 * weight:.2f}")
elif start == "UBP" and end == "BKK":
    print(f"{20 + 40 * weight:.2f}")
elif start == "BKK" and end == "PKT":
    print(f"{25 + 50 * weight:.2f}")
elif start == "PKT" and end == "CNX":
    print(f"{30 + 60 * weight:.2f}")
elif start == "UBP" and end == "PKT":
    print(f"{40 + 70 * weight:.2f}")
else:
    print("Error")
