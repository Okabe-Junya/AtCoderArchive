import math

L = []
N = int(input())
for _ in range(N):
    x, y, P = map(int, input().split())
    L.append((x, y, P))

d = [[10 ** 9] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        d[i][j] = abs(L[i][0] - L[j][0]) + abs(L[i][1] - L[j][1])
        d[i][j] /= L[i][2]

for i in range(N):
    for j in range(N):
        for k in range(N):
            tmp1 = (abs(L[i][0] - L[k][0]) + abs(L[i][1] - L[k][1])) / L[i][2]
            tmp2 = (abs(L[j][0] - L[k][0]) + abs(L[j][1] - L[k][1])) / L[k][2]
            if max(tmp1, tmp2) < d[i][j]:
                d[i][j] = max(tmp1, tmp2)

ans = []
for i in range(N):
    ans.append(max(d[i]))

print(math.ceil(min(ans)))