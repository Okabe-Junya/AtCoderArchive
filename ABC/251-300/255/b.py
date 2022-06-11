N, K = map(int, input().split())
A = list(map(int, input().split()))
b = [False] * N
for i in A:
    b[i - 1] = True

L = []
for _ in range(N):
    L.append(list(map(int, input().split())))


ans = 0
for i in range(N):
    if b[i]:
        continue
    tmp = 10 ** 20
    for j in range(N):
        if not b[j]:
            continue
        if i == j:
            continue
        if (L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2 < tmp:
            tmp = (L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2
    ans = max(ans, tmp)
print(pow(ans, 0.5))