import math


N, M = map(int, input().split())
G = [(0, 0)]
T = []
for _ in range(N):
    X, Y = map(int, input().split())
    G.append((X, Y))

for _ in range(M):
    P, Q = map(int, input().split())
    T.append((P, Q))

dp = [
    [[float("inf"), 0]] * (2 ** (N + M)) for _ in range(N + M)
]  # dp[i]: 最小コスト，ブースターの取得数
dp[0][0] = [0, 0]


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# bit dp
for bit in range(2 ** (M + N)):
    for i in range(N + M):
        if dp[i][bit][0] == float("inf"):
            continue
        for j in range(N + M):
            if bit & (1 << j):
                continue
