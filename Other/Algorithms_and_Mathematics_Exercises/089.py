from math import log2

a, b, c = map(int, input().split())
if c == 1:
    print("No")
    exit()
if b >= 60:
    print("Yes")
    exit()
if log2(a) < b * log2(c):
    print("Yes")
else:
    print("No")