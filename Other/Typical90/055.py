#from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
    A[i] %= P

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    tmp = 1
                    tmp *= A[i]
                    tmp %= P
                    tmp *= A[j]
                    tmp %= P
                    tmp *= A[k]
                    tmp %= P
                    tmp *= A[l]
                    tmp %= P
                    tmp *= A[m]
                    if (tmp % P) == Q:
                        ans += 1
        
print(ans)