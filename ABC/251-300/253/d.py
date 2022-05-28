N, A, B = map(int, input().split())
ans = N * (N + 1) // 2

def gcd(a, b):
    if a < b:  # let a >= b
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


# 最小公倍数
def lcm(a, b):
    def gcd(a, b):
        if a < b:  # let a >= b
            a, b = b, a
        if b == 0:
            return a
        return gcd(b, a % b)
    return a * b // gcd(a, b)

Amax = N // A
Asum = A * Amax * (Amax + 1) // 2
Bmax = N // B
Bsum = B * Bmax * (Bmax + 1) // 2
ABmax = N // lcm(A, B)
ABsum = lcm(A, B) * ABmax * (ABmax + 1) // 2

print(ans - Asum - Bsum + ABsum)