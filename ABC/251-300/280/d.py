K = int(input())


def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
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


def factorial(n):  # n > 0
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


arr = factorization(K)
tmp_ans = arr[-1][0]
if tmp_ans >= 100:
    print(tmp_ans * arr[-1][-1])
else:
    tmp = factorial(tmp_ans)
    while True:
        if tmp % K == 0:
            print(tmp_ans)
            break
        else:
            tmp_ans += 1
            tmp *= tmp_ans
