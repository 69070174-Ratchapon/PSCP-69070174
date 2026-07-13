"""rabbitt"""
w,l,h = map(int,input().split())
price = int(input())
result = ((w * 2) + (l * 2)) * h
print(result)
print(price * result)
