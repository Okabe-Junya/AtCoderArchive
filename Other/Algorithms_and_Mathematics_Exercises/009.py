N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = True
    
for i in range(1, N + 1):
    for j in range(1, S + 1):
        dp[i][j] = dp[i - 1][j] 
        if j >= A[i - 1]:
            dp[i][j] |= dp[i - 1][j - A[i - 1]]

#print(dp) 
if dp[N][S]:
    print("Yes")
else:
    print("No")