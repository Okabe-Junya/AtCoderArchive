n = int(input())


# 約数列挙
def make_divistors(n):
    lower_divistors, upper_divistors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divistors.append(i)
            upper_divistors.append(n // i)
        i += 1
    return lower_divistors + upper_divistors[::-1]


l = make_divistors(n)
a = len(l) // 2
print(max(len(str(l[a-1])), len(str(l[a]))))
