import heapq

N, M, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = map(int, input().split())
    G[A - 1].append((B - 1, T, K))
    G[B - 1].append((A - 1, T, K))

def dijkstra(adj, n, s=0):  # adj: 隣接行列，n: ノード数，s: 始点ノード
    INF = float('inf')
    d = [INF] * n # 始点からの最短距離
    d[s] = 0 # 始点ノードの距離は0
    seen = [False] * n # 既に訪れたかどうか
    tmp = [(0, s)] 
    while tmp:
        tmp_list = heapq.heappop(tmp)
        tmp_v = tmp_list[1]
        seen[tmp_v] = True
        for t, c, k in adj[tmp_v]:
            dk = tmp_list[0]
            if not dk % k == 0:
                dk = dk + k - dk % k
            if (d[t] > dk + c) & (not seen[t]):
                d[t] = dk + c
                heapq.heappush(tmp, (d[t], t))
    return d

d = dijkstra(G, N, X - 1)

if d[Y - 1] == float('inf'):
    print(-1)
else:
    print(d[Y - 1])