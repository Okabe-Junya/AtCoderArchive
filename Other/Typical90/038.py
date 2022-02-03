def gcd(m,n):
    r = m % n
    return gcd(n,r) if r else n
# 最小公倍数
def lcm(m,n):
    return (m * n // gcd(m,n))
a, b = map(int,input().split())
ans = lcm(a, b)
if ans > 10 ** 18:
    print('Large')
else:
    print(ans)