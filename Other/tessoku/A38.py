D, N = map(int, input().split())
lim = [24] * D
for _ in range(N):
    L, R, H = map(int, input().split())
    for i in range(L - 1, R):
        lim[i] = min(lim[i], H)

print(sum(lim))
