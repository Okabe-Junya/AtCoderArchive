import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

L = [[False] * (M + 1) for _ in range(M)]
for i in range(N):
    s = math.ceil(-A[i] / (i + 1)) - 1
    g = math.floor((M - A[i]) / (i + 1))
    # print(s, g)
    for j in range(max(0, s), min(M, g + 1)):
        if 0 <= A[i] + (j + 1) * (i + 1) <= M:
            L[j][A[i] + (j + 1) * (i + 1)] = True

# print(L)

for i in L:
    for j in range(M):
        if not i[j]:
            print(j)
            break
