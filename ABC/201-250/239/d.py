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


is_prime, table = sieve(200)
a, b, c, d = map(int, input().split())
#print(is_prime)
for i in range(a, b + 1):
    for j in range(c, d + 1):
        #print(i, j)
        if is_prime[i + j - 1]:
            break
    else:
        print("Takahashi")
        exit()
print("Aoki")