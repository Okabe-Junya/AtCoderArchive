from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


n = int(input())
x = list(map(int, input().split()))

r = []
for i in x:
    row = []
    l = factorization(i)
    for i in l:
        row.append(i[0])
    r.append(row)
ans = 1
dp = [[1]]
for i in r:
    row = []
    for j in range(len(dp[-1])):
        for k in i:
            row.append(lcm(dp[-1][j], k))
        row = set(row)
        row = list(row)
    dp.append(row)
print(min(dp[-1]))
