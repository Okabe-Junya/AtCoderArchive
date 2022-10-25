N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [float('inf')] * (N + 1)
prev = [0] * (N + 1)
dp[0] = 0
dp[1] = 0
dp[2] = A[0]
prev[2] = 1
for i in range(3, N + 1):
    if dp[i - 1] + A[i - 2] > dp[i - 2] + B[i - 3]:
        dp[i] = dp[i - 2] + B[i - 3]
        prev[i] = i - 2
    else:
        dp[i] = dp[i - 1] + A[i - 2]
        prev[i] = i - 1

tmp = N
ans_list = [N]
while tmp > 0:
    tmp = prev[tmp]
    ans_list.append(tmp)
ans_list.pop()
print(len(ans_list))
print(*ans_list[::-1])
