import math
import bisect

def solve(a, b):
    return a ** 3 + b ** 3 + a ** 2 * b + a * b ** 2

N = int(input())
L = []
Amax = math.ceil(pow(N, 1/3))
Bmax = math.floor(pow(N/4, 1/3))
#print(Amax, Bmax)
for i in range(Bmax, Amax + 1): # b
    pl = 0
    pr = Bmax
    pc = (pl + pr) // 2
    while pl <= pr:
        tmp = solve(i, pc)
        if tmp < N:
            pl = pc + 1
        else:
            pr = pc - 1
        pc = (pl + pr) // 2
    L.append(solve(i, pc + 1))
L.sort()


def lower_bound(num_list, ky):
    pl = bisect.bisect_left(num_list, ky)
    #pr = bisect.bisect_right(num_list, ky)
    return pl

idx = lower_bound(L, N)
while L[idx] < N:
    idx += 1
print(L[idx])
