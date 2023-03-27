N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
B = set(B)
X = int(input())

dp = [False] * (X + 1)
dp[0] = True
for i in range(1, X + 1):
    for a in A:
        if i - a >= 0:
            dp[i] = dp[i] or dp[i - a]
            if i in B:
                dp[i] = False
print('Yes' if dp[X] else 'No')
