"""asd"""
w, h, m, n = map(int, input().split())

x = [0] + list(map(int, input().split())) + [w]
y = [0] + list(map(int, input().split())) + [h]

widths = []
heights = []

for i in range(m + 1):
    widths.append(x[i + 1] - x[i])

for i in range(n + 1):
    heights.append(y[i + 1] - y[i])

widths.sort(reverse=True)
heights.sort(reverse=True)

first = widths[0] * heights[0]
second = max(
    widths[0] * heights[1],
    widths[1] * heights[0]
)
print(first, second)
