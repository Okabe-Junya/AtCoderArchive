import math
x, y, z = map(int, input().split())
a = y / x
for i in range(10**7):
    if a <= i / z:
        print(i-1)
        break
