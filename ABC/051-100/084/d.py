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


is_2017 = [False] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1, 2):
    if (len(make_divistors(i)) == 2) & (len(make_divistors((i + 1) // 2)) == 2):
        # print(i)
        is_2017[i] = True

is_2017_sum = [0] * (10 ** 5 + 1)
for i in range(1, 10 ** 5 + 1):
    is_2017_sum[i] = is_2017_sum[i - 1] + is_2017[i]

Q = int(input())
# print(is_2017_sum[:10])
for _ in range(Q):
    l, r = map(int, input().split())
    print(is_2017_sum[r + 1] - is_2017_sum[l - 1])
