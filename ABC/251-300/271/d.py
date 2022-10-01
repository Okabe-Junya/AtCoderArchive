N, S = map(int, input().split())
L = []
for _ in range(N):
    a, b = map(int, input().split())
    L.append((a, b))

dp = [[False] * (S + 1) for _ in range(N)]
if L[0][0] <= S:
    dp[0][L[0][0]] = True
if L[0][1] <= S:
    dp[0][L[0][1]] = True
prev = [[-1] * (S + 1) for _ in range(N)]
if L[0][0] <= S:
    prev[0][L[0][0]] = 0
if L[0][1] <= S:
    prev[0][L[0][1]] = 1

for i in range(1, N):
    for j in range(1, S + 1):
        if j - L[i][0] >= 0:
            dp[i][j] |= dp[i - 1][j - L[i][0]]
            if dp[i - 1][j - L[i][0]]:
                prev[i][j] = 0
        if j - L[i][1] >= 0:
            dp[i][j] |= dp[i - 1][j - L[i][1]]
            if dp[i - 1][j - L[i][1]]:
                prev[i][j] = 1

# print(dp)
# print(prev)

if dp[-1][-1]:
    print('Yes')
    ans = ''
    for i in range(N - 1, -1, -1):
        if prev[i][S] == 0:
            ans += 'H'
            S -= L[i][0]
        else:
            ans += 'T'
            S -= L[i][1]
    print(ans[::-1])
else:
    print('No')
