def dijkstra(adj, n, s=0):  # adj: 隣接行列，n: ノード数，s: 始点ノード
    import heapq

    INF = float('inf')
    dist = [INF] * n  # 始点からの最短距離
    dist[s] = 0  # 始点ノードの距離は0
    seen = [False] * n  # 既に訪れたかどうか
    tmp = [(0, s)]
    while tmp:
        tmp_v = heapq.heappop(tmp)[1]
        if seen[tmp_v]:
            continue
        seen[tmp_v] = True
        for t, c, d in adj[tmp_v]:
            if (dist[t] > dist[tmp_v] + c) & (not seen[t]):
                dist[t] = dist[tmp_v] + c
                if d:
                    dist[t] -= 1
                heapq.heappush(tmp, (dist[t], t))
    return dist[-1]


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    G[a - 1].append((b - 1, c * (10 ** 8), d))
    G[b - 1].append((a - 1, c * (10 ** 8), d))

res = dijkstra(G, N)
tree_num = 10 ** 8 - res % (10 ** 8)
print((res + tree_num) // (10 ** 8), tree_num)
