def warshall_floyd(d):  # d[i][j]: (ノードiからノードjへの距離, price)
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if d[i][k][0] == 10**9 or d[k][j][0] == 10**9:
                    continue
                if (
                    d[i][j][0] >= d[i][k][0] + d[k][j][0]
                    and d[i][j][1] < d[i][k][1] + d[k][j][1]
                ):
                    d[i][j] = (d[i][k][0] + d[k][j][0], d[i][k][1] + d[k][j][1])
    return d


N = int(input())
A = list(map(int, input().split()))
G = [[(10**9, 0)] * N for _ in range(N)]
for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == "Y":
            G[i][j] = (1, A[j])

G = warshall_floyd(G)

Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    if G[U][V][0] == 10**9:
        print("Impossible")
    else:
        print(G[U][V][0], G[U][V][1] + A[U])
