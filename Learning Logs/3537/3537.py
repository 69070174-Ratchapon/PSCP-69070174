"""imposter"""
alive = {}
dead = {}

while True:
    line = input().strip()

    if line == "Start":
        break

    name, role = line[1:-1].split(":", 1)
    name = name.strip().strip('"')
    role = role.strip().strip('"')

    alive[name] = role

while True:
    name = input().strip()

    if name == "End":
        break

    if name in alive:
        dead[name] = alive.pop(name)

impostors = 0

for role in alive.values():
    if role == "Impostor":
        impostors += 1

print(f"{impostors} Impostor Remains")

print("***Alive***")
for name in sorted(alive):
    print(f"{name} : {alive[name]}")

print("***Dead***")
for name in sorted(dead):
    print(f"{name} : {dead[name]}")
