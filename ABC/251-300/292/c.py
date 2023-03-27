N = int(input())
ans = 0
tmp = [0] * (N + 1)


def make_divistors(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            if i != n // i:
                upper.append(n // i)
        i += 1
    return lower + upper[::-1]


for i in range(1, N):
    tmp[i] = len(make_divistors(i))


for i in range(1, N):
    n1 = i
    n2 = N - i
    ans += tmp[n1] * tmp[n2]
print(ans)
