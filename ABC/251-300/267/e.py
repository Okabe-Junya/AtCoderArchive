N, M = map(int, input().split())
A = list(map(int, input().split()))
G = {}
for _ in range(M):
    u, v = map(int, input().split())
    if (u - 1) not in G:
        G[u - 1] = set()
    if (v - 1) not in G:
        G[v - 1] = set()
    G[u-1].add(v-1)
    G[v-1].add(u-1)

count = [0] * N
for i in range(N):
    for j in G[i]:
        count[i] += A[j]

start = count.index(min(count))
ans = min(count)
for i in range(N - 1):
    min_count = 10 ** 9
    G.pop(start, None)
    count[start] = None
    for j in G:
        if count[j] is None:
            continue
        if start in G[j]:
            count[j] -= A[start]
        if count[j] < min_count:
            min_count = count[j]
            start = j
        G[j].discard(start)
    if min_count > ans:
        ans = min_count
print(ans)
