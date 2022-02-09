# 素因数分解
def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


n = int(input())
res = factorization(n)
for i in res:
    for j in range(i[1]):
        print(i[0])