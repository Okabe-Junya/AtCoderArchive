import math

INF = 998244353

N = int(input())
m = math.floor(math.sqrt(N))
ans = 0
for i in range(1, m + 1):
    ans += (N // i - i) // 2 + 1
    ans %= INF
print(ans % INF)