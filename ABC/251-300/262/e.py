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

cmb_zero = 1
cmb_one = 1
i = -2
flag = False
while i <= K:
    i += 2
    zero = K - i
    one = i
    if zero > dict[0] or one > dict[1]:
        continue
    if flag == False:
        cmb_zero = cmb(dict[0], dict[0] - zero)
        cmb_one = cmb(dict[1], one)
        flag = True
    else:
        cmb_zero *= (zero + 1) * (zero + 2)
        cmb_zero //= (dict[0] - zero) * (dict[0] - zero - 1) 
        cmb_one *= (dict[1] - one + 2) * (dict[1] - one + 1)
        cmb_one //= one * (one - 1)
        
    cmb_zero %= INF
    cmb_one %= INF
    ans += cmb_zero * cmb_one
    ans %= INF
print(ans)