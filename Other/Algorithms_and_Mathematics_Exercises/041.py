T = int(input())
N = int(input())
tmp = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    tmp[L] += 1
    tmp[R] -= 1

ans = 0
for i in range(len(tmp) - 1):
    ans += tmp[i]
    print(ans)