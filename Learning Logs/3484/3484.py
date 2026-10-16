"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
n, p = input().split()
n = int(n)
p = float(p)

column_tiles = [0] * n
column_points = [0] * n
total_tiles = 0
total_points = 0

for _ in range(n):
    row = list(map(int, input().split()))
    row_tiles = 0
    row_points = sum(row)

    for j in range(n):
        if row[j] > 0:
            row_tiles += 1
            column_tiles[j] += 1

        column_points[j] += row[j]

    total_tiles += row_tiles
    total_points += row_points

    print(*row, row_tiles, row_points)

print(*column_tiles)
print(*column_points)
print(total_tiles, total_points, f"{total_points * p:.2f}")
