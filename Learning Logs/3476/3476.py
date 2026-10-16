"""CuteCat CuteFox"""
animals = {}

for _ in range(int(input())):
    data = input().strip()[1:-1]

    for pair in data.split(","):
        name, number = pair.split(":")
        name = name.strip().strip("\"'")
        number = number.strip().strip("\"'")
        animals[name] = number

if "Garfield" not in animals and "Cat01" not in animals.values():
    animals["Garfield"] = "Cat01"

if "Fubuki" not in animals and "Fox01" not in animals.values():
    animals["Fubuki"] = "Fox01"

cats = {}
foxes = {}

for name, number in animals.items():
    if number.startswith("Cat"):
        cats[number] = name
    else:
        foxes[number] = name

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

for number in sorted(cats, key=lambda x: int(x[3:])):
    print(f"{cats[number]} : {number}")

for number in sorted(foxes, key=lambda x: int(x[3:])):
    print(f"{foxes[number]} : {number}")
