W = int(input())

# エラトステネスの篩
def sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    for i in range(2, n + 1):
        if is_prime[i - 1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n + 1) if is_prime[i - 1]]
    return is_prime, table

_, res = sieve(10 ** 6)
ans = [1]
for i in ans:
    tmp = ans[-1] * 2
    if tmp >= 10 ** 6:
        break
    ans.append(tmp)
tmp = 1
while tmp <= 10 ** 6:
    ans.append(tmp)
    tmp *= 3


print(ans)
print(len(ans))