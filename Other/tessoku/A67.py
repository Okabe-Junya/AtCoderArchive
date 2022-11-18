def prim(adj):
    import heapq

    # adj: 隣接行列
    # adj[i]: i番目のノードに接続するノードのリスト（cost, node）の順
    N = len(adj)  # ノード数
    res_set = set()  # 最小全域木のノード集合
    seen = [False] * N  # 既に訪れたかどうか
    res = 0  # 最小全域木の重みの合計
    heap = [(0, 0)]  # (cost, node)の順でソートするためのheap
    heapq.heapify(heap)
    while heap:
        cost, node = heapq.heappop(heap)
        if seen[node]:
            continue

        seen[node] = True
        res_set.add(node)
        res += cost

        for c, t in adj[node]:
            if not seen[t]:
                heapq.heappush(heap, (c, t))

        if len(res_set) == N:
            break
    return res


N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((c, b - 1))
    G[b - 1].append((c, a - 1))

print(prim(G))
