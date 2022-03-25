INF = 998244353

N, M, K, S, T, X = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    

dp = [[[0, 0] for _ in range(K + 1)] for _ in range(N)] 
# dp[[i][j][0]] : Aj = i かつXを偶数回踏んでいる場合のかず
# dp[[i][j][1]] : Aj = i かつXを奇数回踏んでいる場合のかず

dp[S - 1][0][0] = 1
for i in range(1, K + 1):
    for j in range(N):
        for k in G[j]:
            if k != X - 1:
                dp[k][i][0] += dp[j][i - 1][0]
                dp[k][i][1] += dp[j][i - 1][1]
            else:
                dp[k][i][1] += dp[j][i - 1][0]
                dp[k][i][0] += dp[j][i - 1][1]
            dp[k][i][0] %= INF
            dp[k][i][1] %= INF
print(dp[T - 1][K][0] % INF)