import math
a, b, d = map(int, input().split())
a_ = a * math.cos(math.radians(d)) - b * math.sin(math.radians(d))
b_ = a * math.sin(math.radians(d)) + b * math.cos(math.radians(d))
print(a_, b_)