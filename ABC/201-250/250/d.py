import bisect

# 二分探索（lower_bound）
def lower_bound(num_list, ky):
    #pl = bisect.bisect_left(num_list, ky)
    pr = bisect.bisect_right(num_list, ky)
    return pr


N = int(input())


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
    return table


ans = 0
table = sieve(10 ** 6)
for i in range(len(table)):
    tmp = N // (table[i] ** 3)
    res = min(i, lower_bound(table, tmp))
    ans += res
print(ans)
