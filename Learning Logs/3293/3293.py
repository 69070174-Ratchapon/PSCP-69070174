"""frame"""
list1 = []
maximum = 0
for i in range(5):
    list1.append(input().strip())
for i in list1:
    if len(i) > maximum:
        maximum = len(i)
print("*" * (maximum + 4))
print(f"* {list1[0]}{" " * (maximum - len(list1[0]))} *")
print(f"* {list1[1]}{" " * (maximum - len(list1[1]))} *")
print(f"* {list1[2]}{" " * (maximum - len(list1[2]))} *")
print(f"* {list1[3]}{" " * (maximum - len(list1[3]))} *")
print(f"* {list1[4]}{" " * (maximum - len(list1[4]))} *")
print("*" * (maximum + 4))
