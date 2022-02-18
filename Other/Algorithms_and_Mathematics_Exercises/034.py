from itertools import combinations as cmb
from math import sqrt

n = int(input())
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x, y))

ans = 10 ** 9
for b in cmb(l, 2):
    a0 = b[0]
    a1 = b[1]
    tmp = (a0[0] - a1[0])**2 + (a0[1] - a1[1])**2
    if tmp < ans:
        ans = tmp
print(sqrt(ans))
