Q = int(input())


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
    return is_prime, table


_, table = sieve(300000)
prime_set = set(table)

for _ in range(Q):
    X = int(input())
    print('Yes' if X in prime_set else 'No')
