N = int(input())
h = list(map(int, input().split()))

dp = [float("inf") for _ in range(N)]
dp[0] = 0
dp[1] = abs(h[1] - h[0])
prev = [-1 for _ in range(N)]
prev[1] = 0
for i in range(2, N):
    if dp[i - 1] + abs(h[i] - h[i - 1]) > dp[i - 2] + abs(h[i] - h[i - 2]):
        dp[i] = dp[i - 2] + abs(h[i] - h[i - 2])
        prev[i] = i - 2
    else:
        dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])
        prev[i] = i - 1

ans = [N]
tmp = N - 1
while tmp != 0:
    tmp = prev[tmp]
    ans.append(tmp + 1)
print(len(ans))
print(*reversed(ans))
