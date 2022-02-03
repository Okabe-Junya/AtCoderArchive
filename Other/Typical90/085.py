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
l = make_divistors(k)
ans = 0
for a in l:
    for b in l:
        if a > b:
            continue
        if k % (a * b) == 0:
            c = k // (a * b)
            if b > c:
                continue
            #print(a, b, k // (a * b))
            ans += 1
print(ans)
