import math
n = int(input())
a = 2 * math.pi / n
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x = (x1 + x2) / 2
y = (y1 + y2) / 2
xa = (x1 - x) * math.cos(a) - (y1 - y) * math.sin(a)
ya = (y1 - y) * math.cos(a) + (x1 - x) * math.sin(a)
print(xa + x, ya + y)
