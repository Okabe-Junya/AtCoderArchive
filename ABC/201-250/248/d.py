N = int(input())
A = list(map(int, input().split()))
Q = int(input())

import bisect

def lower_bound(num_list, ky):
    pl = bisect.bisect_left(num_list, ky)
    pr = bisect.bisect_right(num_list, ky)
    return pl, pr

l = [[] for _ in range(N)]
for i in range(N):
    l[A[i] - 1].append(i)
# print(l)
for _ in range(Q):
    L, R, X = map(int, input().split())
    if len(l[X - 1]) == 0:
        print(0)
        continue
    elif len(l[X - 1]) == 1:
        if l[X - 1][0] >= L - 1 and l[X - 1][0] <= R - 1:
            print(1)
        else:
            print(0)
        continue
    pl, _ = lower_bound(l[X - 1], L - 1)
    _, pr = lower_bound(l[X - 1], R - 1)
    print(pr - pl)