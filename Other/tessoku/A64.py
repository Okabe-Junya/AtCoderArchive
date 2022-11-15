import heapq


def dijkstra(adj, n, s=0):  # adj: 隣接行列，n: ノード数，s: 始点ノード
    INF = float("inf")
    d = [INF] * n  # 始点からの最短距離
    d[s] = 0  # 始点ノードの距離は0
    seen = [False] * n  # 既に訪れたかどうか
    tmp = [(0, s)]
    while tmp:
        tmp_v = heapq.heappop(tmp)[1]
        if seen[tmp_v]:
            continue
        seen[tmp_v] = True
        for t, c in adj[tmp_v]:
            if (d[t] > d[tmp_v] + c) & (not seen[t]):
                d[t] = d[tmp_v] + c
                heapq.heappush(tmp, (d[t], t))
    return d


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, c))

d = dijkstra(G, N)
for i in range(N):
    if d[i] == float("inf"):
        print(-1)
    else:
        print(d[i])
