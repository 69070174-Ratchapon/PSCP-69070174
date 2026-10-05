"""PrimeNumber"""
start,end = map(int,input().split())
q = ""
count = 0
for j in range(start,end+1):
    if j < 2:
        continue
    prime = True
    for i in range(2,int(j / 2) + 1):
        if not j % i:
            prime = False
            break
    if prime:
        q += str(j) + " "
        count += 1
if not count:
    print(f"Total primes: {count}")
else:
    print(q.strip())
    print(f"Total primes: {count}")
