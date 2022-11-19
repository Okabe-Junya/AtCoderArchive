N = int(input())
L = []
for _ in range(N):
    S = input()
    L.append(S)

G = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if L[i][-1] == L[j][0]:
            G[i].append(j)


# 巡回セールスマン問題
dp = [[0] * N for _ in range(1 << N)]
for i in range(N):
    dp[1 << i][i] = 1

for S in range(1 << N):
    for v in range(N):
        if dp[S][v] == 0:
            continue
        flag = False
        for nv in G[v]:
            if S & (1 << nv):
                continue
            dp[S | (1 << nv)][nv] += dp[S][v]
            flag = True
        if not flag:
            if bin(S).count("1") % 2 != 0:
                print("First")
                exit()
            else:
                print("Second")
                exit()
