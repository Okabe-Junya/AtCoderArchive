def make_divistors(n):
    lower_divistors, upper_divistors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divistors.append(i)
            if i != n // i:
                upper_divistors.append(n // i)
        i += 1
    return lower_divistors + upper_divistors[::-1]


k = int(input())
dp = [0 for i in range(k+1)]
l = []
ans = 0
for i in range(k+1):
    tmp = 0
    a = make_divistors(i)
    l.append(a)
    for j in a:
        tmp += len(l[j])
    dp[i] = dp[i-1] + tmp
print(dp[-1])
