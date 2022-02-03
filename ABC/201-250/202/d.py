from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n-r, -1))
    under = reduce(mul, range(1, r+1))
    return over // under


a, b, k = map(int, input().split())
c = a + b
tmp = 0
s = cmb(a+b, b)
for i in range(a+b):
    if a == 0:
        print('b' * (c-i))
        break
    if b == 0:
        print('a' * (c-i))
        break
    if k <= tmp + cmb(a+b-1, a-1):
        print('a', end='')
        a -= 1
    else:
        print('b', end='')
        tmp += cmb(a+b-1, a-1)
        b -= 1
