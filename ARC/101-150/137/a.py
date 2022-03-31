from math import gcd


L, R = map(int, input().split())
MAX = R - L
for i in range(MAX, 0, -1):
    tmpL, tmpR = L, L + i
    while tmpR <= R:
        if gcd(tmpL, tmpR) == 1:
            print(i)
            exit()
        tmpL += 1
        tmpR += 1
print(1)