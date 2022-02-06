# 最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)

n, x, y = map(int, input().split())
print((n // x) + (n // y) - (n // lcm(x, y)))