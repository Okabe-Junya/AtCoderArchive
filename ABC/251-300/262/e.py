import math

def cmb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

INF = 998244353

N, M, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

ans = 0
dict = {0: 0, 1: 0}
for i in range(N):
    dict[len(G[i]) % 2] += 1

zero = K
one = 0
cmb0 = 1
cmb1 = 1
while one <= K and zero >= 0:
    if dict[0] < zero or dict[1] < one:
        zero -= 2
        one += 2
        continue
    cmb0 *= (zero + 1) * (zero + 2)
    cmb0 //= (dict[0] - zero) * (dict[0] - zero - 1) 
    cmb1 *= (dict[1] - one + 2) * (dict[1] - one + 1)
    cmb1 //= one * (one - 1)
    cmb0 %= INF
    cmb1 %= INF
    ans += cmb(dict[0], zero) * cmb(dict[1], one)
    zero -= 2
    one += 2
    ans %= INF
print(ans)