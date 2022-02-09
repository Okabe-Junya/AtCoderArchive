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


# 最小公倍数（リスト）
def lcm_list(l):
    res = l[0]
    for i in l:
        res = lcm(res, i)
    return res


n = int(input())
a = list(map(int, input().split()))
print(lcm_list(a))