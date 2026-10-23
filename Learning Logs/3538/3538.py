"""fullypair"""
x = input()
result = {}
q = []
for i in x:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for j,c in result.items():
    if c % 2 == 1:
        q.append(j)
if not q:
    print("fully paired")
else:
    print("".join(q))
