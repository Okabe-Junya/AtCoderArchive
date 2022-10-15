from bisect import bisect_left, bisect_right

H, W, rs, cs = map(int, input().split())
N = int(input())
d = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

idx = {}
col = {}

L = []
for _ in range(N):
    r, c = map(int, input().split())
    L.append((r, c))
    if r not in idx:
        idx[r] = [-1, c, W + 1]
    else:
        idx[r].append(c)
    if c not in col:
        col[c] = [-1, r, H + 1]
    else:
        col[c].append(r)

for i in idx:
    idx[i].sort()
for i in col:
    col[i].sort()
# print(idx, col)
L = set(L)

Q = int(input())
for _ in range(Q):
    d, num = input().split()
    num = int(num)
    if d == "L":
        if rs not in idx:
            cs = max(1, cs - num)
        else:
            tmp = bisect_right(idx[rs], cs)
            cs = max(1, cs - num, idx[rs][tmp - 1] + 1)
    elif d == "R":
        if rs not in idx:
            cs = min(W, cs + num)
        else:
            tmp = bisect_left(idx[rs], cs)
            cs = min(W, cs + num, idx[rs][tmp] - 1)
    elif d == "U":
        if cs not in col:
            rs = max(1, rs - num)
        else:
            tmp = bisect_right(col[cs], rs)
            rs = max(1, rs - num, col[cs][tmp - 1] + 1)
    else:
        if cs not in col:
            rs = min(H, rs + num)
        else:
            tmp = bisect_left(col[cs], rs)
            rs = min(H, rs + num, col[cs][tmp] - 1)
    print(rs, cs)
