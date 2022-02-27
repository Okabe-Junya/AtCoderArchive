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


n, m = map(int, input().split())
l = make_divistors(m)
ans = 1
for i in range(len(l)):
    if l[len(l) - 1 - i] < n:
        break
    else:
        ans = l[i]
print(ans)
