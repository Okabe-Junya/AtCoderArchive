N = int(input())


def make_divistors(n):
    lower, upper = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower.append(i)
            upper.append(n // i)
        i += 1
    return lower, upper


l, u = make_divistors(N)
print(2 * (l[-1] + u[-1]))
