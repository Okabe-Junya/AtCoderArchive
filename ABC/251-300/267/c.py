N, M = map(int, input().split())
A = list(map(int, input().split()))
Asum = [0]
for i in range(N):
    Asum.append(Asum[-1] + A[i])

ans = []
tmp = 0
for i in range(M):
    tmp += (i + 1) * A[i]

ans.append(tmp)
for i in range(N - M):
    tmp -= Asum[i + M] - Asum[i]
    tmp += A[i + M] * M
    ans.append(tmp)

print(max(ans))
