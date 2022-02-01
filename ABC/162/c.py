def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n


def g(m, n, r):
    a = gcd(m, n)
    return gcd(a, r)


k = int(input())
ans = 0
for i in range(1, k+1):
    for j in range(1, k+1):
        for l in range(1, k+1):
            ans += g(i, j, l)
print(ans)
