"""gift"""
n,k,t = map(int,input().split())
result = 1
count = 1
result2 = 0
while result != t and result2 != 1:
    result += k
    result %= n
    if not result:
        result = n
    count += 1
    result2 = result
if result2 == 1:
    count -= 1
print(count)
