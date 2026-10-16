""""songtor"""
n, s = map(int, input().split())

next_student = [0] + [int(input()) for _ in range(n)]
visited = [False] * (n + 1)

count = 0
current = s

while current and not visited[current]:
    visited[current] = True
    count += 1
    current = next_student[current]

print(count)
