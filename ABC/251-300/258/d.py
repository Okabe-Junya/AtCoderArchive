N, X = map(int, input().split())
L = []
for _ in range(N):
    A, B = map(int, input().split())
    L.append((A, B))

Asum = [L[0][0] + L[0][1]]
for i in range(1, N):
    Asum.append(Asum[-1] + L[i][0] + L[i][1])

ans = []
for i in range(N):
    if (i + 1) >= X:
        ans.append(Asum[i])
    else:
        time = Asum[i] + (X - (i + 1)) * L[i][1]
        ans.append(time)
print(min(ans))