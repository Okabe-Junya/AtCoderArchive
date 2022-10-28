H, W, N = map(int, input().split())
L = [[0] * (W + 1) for _ in range(H + 1)]

for _ in range(N):
    a, b, c, d = map(int, input().split())
    L[a - 1][b - 1] += 1
    L[c][d] += 1
    L[a - 1][d] -= 1
    L[c][b - 1] -= 1

Lsum = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            Lsum[i][j] = L[i][j]
        elif i == 0:
            Lsum[i][j] = Lsum[i][j - 1] + L[i][j]
        elif j == 0:
            Lsum[i][j] = Lsum[i - 1][j] + L[i][j]
        else:
            Lsum[i][j] = Lsum[i - 1][j] + Lsum[i][j - 1] - Lsum[i - 1][j - 1] + L[i][j]

for row in Lsum:
    print(*row)
