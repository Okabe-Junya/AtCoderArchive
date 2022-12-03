import heapq

N, M, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    G[a - 1].append((b - 1, c))
    G[b - 1].append((a - 1, -c))

seen = [False] * N
uf = [-1] * N
for i in range(N):
    if seen[i]:
        continue
    seen[i] = True
    tmp_node = [i]
    stack = [(i, 0)]
    flag = False  # 正になる閉路があったらTrue
    while stack:
        v, d = stack.pop()
        for u, c in G[v]:
            if seen[u]:
                for node in tmp_node:
                    if uf[node] < d + c:
                        flag = True
                        break
            else:
                seen[u] = True
                tmp_node.append(u)
                stack.append((u, d + c))
    if flag:
        cnt = -i
    else:
        cnt = i
    for v in tmp_node:
        uf[v] = cnt

print(uf)


for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if uf[x] != uf[y]:
        print('nan')
    elif uf[x] < 0:
        print('inf')
    else:
        dist = [-1] * N
        heap = [(0, x)]
        while heap:
            d, v = heapq.heappop(heap)
            if dist[v] != -1:
                continue
            dist[v] = d
            for u, c in G[v]:
                if dist[u] == -1:
                    heapq.heappush(heap, (d + c, u))
        print(dist[y])
