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


N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = {i for i in range(1, M + 1)}
prime = set()
for num in A:
    if num == 1:
        continue
    else:
        arr = factorization(num)
        prime = prime.union({i[0] for i in arr})

prime.discard(1)
for i in prime:
    tmp = {j for j in range(1, M + 1) if j % i == 0}
    ans = ans - tmp
print(len(ans))
for i in sorted(ans):
    print(i)