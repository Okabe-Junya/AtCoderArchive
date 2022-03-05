N, T = map(int, input().split())
t = list(map(int, input().split()))
ans = T * N
tmp = 0
for i in range(N - 1):
    if t[i + 1] - t[i] <= T:
        ans -= T - (t[i + 1] - t[i])
print(ans)
