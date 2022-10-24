H, W = map(int, input().split())
X = []
for _ in range(H):
    x = list(map(int, input().split()))
    X.append(x)


Xsum = [[0] * (W + 1) for _ in range(H + 1)]
Xsum[1][1] = X[0][0]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        Xsum[i][j] = Xsum[i - 1][j] + Xsum[i][j - 1] - Xsum[i - 1][j - 1] + X[i - 1][j - 1]

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(Xsum[c][d] - Xsum[a - 1][d] - Xsum[c][b - 1] + Xsum[a - 1][b - 1])
