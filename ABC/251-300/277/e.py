from collections import deque

N, M, K = map(int, input().split())
G0 = [[] for _ in range(N)]
G1 = [[] for _ in range(N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    if a == 0:
        G0[u - 1].append(v - 1)
        G0[v - 1].append(u - 1)
    else:
        G1[u - 1].append(v - 1)
        G1[v - 1].append(u - 1)

s = list(map(int, input().split()))
s = set(s)

# print(G0, G1, s)
seen = [[-1, -1] for _ in range(N)]
seen[0][1] = 0
queue = deque()
queue.append((0, 1))
while queue:
    # print(queue)
    v, a = queue.popleft()
    if a == 0:
        for u in G0[v]:
            if seen[u][0] == -1:
                seen[u][0] = seen[v][0] + 1
                queue.append((u, 0))
    if a == 1:
        for u in G1[v]:
            if seen[u][1] == -1:
                seen[u][1] = seen[v][1] + 1
                queue.append((u, 1))
    if v + 1 in s:
        a = 1 - a
        if seen[v][a] == -1:
            seen[v][a] = seen[v][1 - a]
            queue.append((v, a))

if seen[N - 1][0] == -1 and seen[N - 1][1] == -1:
    print(-1)
else:
    if seen[N - 1][0] == -1:
        print(seen[N - 1][1])
    elif seen[N - 1][1] == -1:
        print(seen[N - 1][0])
    else:
        print(min(seen[N - 1][0], seen[N - 1][1]))
