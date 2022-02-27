n, m = map(int, input().split())
dp = [1 for _ in range(n + 1)]
l = [0 for _ in range(m)]
INF = 10 ** 9 + 7
for i in range(m):
    a = int(input())
    l[i] = a
for j in l:
    dp[j] = False
dp[0] = 1
if dp[1]:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(n - 1):
    if dp[i + 2]:
        dp[i + 2] = (dp[i + 1] + dp[i]) % INF
    else:
        dp[i + 2] = 0
print(dp[-1] % INF)
