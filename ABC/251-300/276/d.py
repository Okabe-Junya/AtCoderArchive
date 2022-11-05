N = int(input())
A = list(map(int, input().split()))
ans = 0

A2 = []
for i in range(N):
    tmp = A[i]
    while tmp % 2 == 0:
        ans += 1
        tmp //= 2
    while tmp % 3 == 0:
        ans += 1
        tmp //= 3
    if i == 0:
        A2.append(tmp)
    else:
        if A2[-1] == tmp:
            continue
        else:
            print(-1)
            exit()


def gcd_list(l):
    def gcd(a, b):
        if a < b:  # let a >= b
            a, b = b, a
        if b == 0:
            return a
        return gcd(b, a % b)

    res = l[0]
    for num in l:
        res = gcd(res, num)
    return res


gcdA = gcd_list(A)
while gcdA % 2 == 0:
    ans -= N
    gcdA //= 2
while gcdA % 3 == 0:
    ans -= N
    gcdA //= 3
print(ans)
