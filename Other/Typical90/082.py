l, r = map(int, input().split())
ans = 0
INF = 10 ** 9 + 7

def sum_a_b(a, b): # a~b の和
    return ((a + b) * (b - a + 1)) // 2

l_keta = len(str(l))
r_keta = len(str(r))
if l_keta == r_keta:
    print((l_keta * (l + r) * (r - l + 1) // 2) % INF)
else:
    for i in range(l_keta, r_keta + 1):
        if i == l_keta:
            ma = 10 ** l_keta - 1
            ans += sum_a_b(l, ma) * l_keta
        elif i == r_keta:
            mi = 10 ** (r_keta - 1)
            ans += sum_a_b(mi, r) * r_keta
        else:
            mi = 10 ** (i - 1)
            ma = 10 ** i - 1
            ans += sum_a_b(mi, ma) * i
        ans %= INF
    print(ans)