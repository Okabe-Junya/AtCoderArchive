N = int(input())

six_list = [1]
nine_list = [1]

while six_list[-1] < 10 ** 6:
    six_list.append(six_list[-1] * 6)

while nine_list[-1] < 10 ** 6:
    nine_list.append(nine_list[-1] * 9)

nums = list(set(six_list + nine_list))
INF = 10 ** 9
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(1, len(dp)):
    for num in nums:
        if i >= num:
            dp[i] = min(dp[i], dp[i - num] + 1)
print(dp[N])