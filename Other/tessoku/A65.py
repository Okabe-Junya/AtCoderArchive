N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
G = [[] for _ in range(N)]
for i in range(N - 1):
    # print(G)
    G[A[i] - 1].append(i + 1)

for i in range(N - 2, -1, -1):
    if not G[i]:
        continue
    for j in G[i]:
        dp[i] += dp[j] + 1
print(*dp)
