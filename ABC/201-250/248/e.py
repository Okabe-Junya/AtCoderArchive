from itertools import combinations as cmb

# 最大公約数
def gcd(a, b):
    if a < b:  # let a >= b
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

N, K = map(int, input().split())
A = []
L = []
for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))
ans = 0
if K == 1:
    print("Infinity")
    exit()

for i in cmb(range(N), 2):
    x1, y1 = A[i[0]][0], A[i[0]][1]
    x2, y2 = A[i[1]][0], A[i[1]][1]
    d = [x2 - x1, y2 - y1]
    if d[0] != 0:
        s = y1 - x1 * d[1] / d[0]
    else:
        s = x1
    L.append((d, s))
s = []
for i in range(len(L)):
    tmpx, tmpy = abs(L[i][0][0]), abs(L[i][0][1])
    g = gcd(tmpx, tmpy)
    L[i][0][0] = L[i][0][0] // g
    L[i][0][1] = L[i][0][1] // g
    if tmpx == 0:
        s.append((0, 1, L[i][1]))
    elif tmpy == 0:
        s.append((1, 0, L[i][1]))
    else:
        s.append((L[i][0][0], L[i][0][1], L[i][1]))
s = set(s)
for i in s:
    cnt = 0
    dx, dy, z = i[0], i[1], i[2]
    for i in range(N):
        x, y = A[i][0], A[i][1]
        if cnt == K:
            ans += 1
            break
        if dx != 0:
            if abs (x * (dy / dx) + z - y) < 1e-7:
                cnt += 1
        else:
            if x == z:
                cnt += 1
print(ans)