x = int(input())


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


while True:
    l = make_divistors(x)
    if len(l) == 2:
        print(x)
        break
    else:
        x += 1
