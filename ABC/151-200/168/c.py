import math

a, b, h, m = map(int, input().split())

hr = 30 * h + 0.5 * m
mr = 6 * m
r = abs(hr - mr)
r = min(r, 360 - r)
# print(math.cos(r * math.pi / 180))
ans = a ** 2 + b ** 2 - 2 * a * b * math.cos(r * math.pi / 180)
print(math.sqrt(ans))