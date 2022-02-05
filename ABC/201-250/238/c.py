INF = 998244353
n = int(input())
k = len(str(n))
ans = 45
if  k == 1:
    print(n * (n + 1) // 2)
    exit()
else:
    for i in range(2, k):
        m = 9 * (10 ** (i - 1))
        ans += m * (m + 1) // 2
        ans %= INF
    ans += (n - 10 ** (k - 1) + 1) * (n - 10 ** (k - 1) + 2) // 2
print(ans % INF)