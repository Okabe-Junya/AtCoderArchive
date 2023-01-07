from math import sqrt


def sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False
    for i in range(2, n + 1):
        if is_prime[i - 1]:
            j = 2 * i
            while j <= n:
                is_prime[j - 1] = False
                j += i
    table = [i for i in range(1, n + 1) if is_prime[i - 1]]
    return table


prime = sieve(3 * 10**6)


T = int(input())
for _ in range(T):
    N = int(input())
    for i in prime:
        if N % i == 0:
            tmpN = N // i
            if tmpN % i == 0:
                print(i, tmpN // i)
                break
            else:
                print(int(sqrt(tmpN)), i)
                break
