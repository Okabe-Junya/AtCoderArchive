# 約数列挙
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


n = int(input())
l = make_divistors(n)
s = sum(l) - n
if n == s:
    print('Perfect')
elif n > s:
    print('Deficient')
else:
    print('Abundant')
