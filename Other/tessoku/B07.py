T = int(input())
N = int(input())
S = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    S[L] += 1
    S[R] -= 1

ans = 0
for i in range(T):
    ans += S[i]
    print(ans)
