def gcd(a, b):
    if a < b:  # let a >= b
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    def gcd(a, b):
        if a < b:  # let a >= b
            a, b = b, a
        if b == 0:
            return a
        return gcd(b, a % b)

    return a * b // gcd(a, b)


a, b = map(int, input().split())
print(lcm(a, b))
