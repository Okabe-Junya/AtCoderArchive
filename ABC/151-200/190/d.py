n = int(input())
ans = 0


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


a = make_divistors(2 * n)
b = list(reversed(a))
for i in range(len(a)):
    if (a[i] - b[i]) % 2 == 1:
        ans += 1
print(ans)
