N = int(input())
L = [[0] * 1500 for _ in range(1500)]
for _ in range(N):
    x, y = map(int, input().split())
    L[x - 1][y - 1] += 1

Lsum = [[0] * 1500 for _ in range(1500)]
for i in range(1500):
    Lsum[i][0] = L[i][0]

for i in range(1500):
    for j in range(1, 1500):
        Lsum[i][j] = Lsum[i][j - 1] + L[i][j]

for i in range(1, 1500):
    for j in range(1500):
        Lsum[i][j] += Lsum[i - 1][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    if a == 1 and b == 1:
        print(Lsum[c - 1][d - 1])
    elif a == 1:
        print(Lsum[c - 1][d - 1] - Lsum[c - 1][b - 2])
    elif b == 1:
        print(Lsum[c - 1][d - 1] - Lsum[a - 2][d - 1])
    else:
        print(
            Lsum[c - 1][d - 1]
            - Lsum[a - 2][d - 1]
            - Lsum[c - 1][b - 2]
            + Lsum[a - 2][b - 2]
        )
