import math
r, x, y = map(int, input().split())
d = x ** 2 + y ** 2
if d < r ** 2:
    print(2)
    exit()
k = d / (r ** 2)
print(math.ceil(math.sqrt(k)))
