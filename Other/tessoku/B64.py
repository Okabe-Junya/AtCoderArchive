def dijkstra(adj, n, s=0):  # adj: 隣接行列，n: ノード数，s: 始点ノード
    import heapq

    INF = 10**9
    dist = [INF] * n  # 始点からの最短距離
    prev = [-1] * n  # 一つ前
    dist[s] = 0  # 始点ノードの距離は0
    seen = [False] * n  # 既に訪れたかどうか
    tmp = [(0, s)]
    while tmp:
        tmp_v = heapq.heappop(tmp)[1]
        seen[tmp_v] = True
        for t, c in adj[tmp_v]:
            if (dist[t] > dist[tmp_v] + c) & (not seen[t]):
                dist[t] = dist[tmp_v] + c
                prev[t] = tmp_v
                heapq.heappush(tmp, (dist[t], t))
    root = [n]
    tmp_node = n - 1
    while tmp_node != 0:
        root.append(prev[tmp_node] + 1)
        tmp_node = prev[tmp_node]
    return root[::-1]


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))

rest = dijkstra(G, N, 0)
print(*rest)
