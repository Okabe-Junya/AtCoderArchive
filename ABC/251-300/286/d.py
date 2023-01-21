N, X = map(int, input().split())
L = []
for _ in range(N):
    A, B = map(int, input().split())
    L.append((A, B))

dp = [[False] * (X + 1) for _ in range(N)]
for i in range(L[0][1] + 1):
    if i * L[0][0] <= X:
        dp[0][i * L[0][0]] = True

for i in range(N - 1):
    for j in range(X + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            for k in range(L[i + 1][1] + 1):
                if j + k * L[i + 1][0] <= X:
                    dp[i + 1][j + k * L[i + 1][0]] = True

# print(dp)
print('Yes' if dp[N - 1][X] else 'No')
