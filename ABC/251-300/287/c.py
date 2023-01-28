N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

Z = [0] * N
for i in range(N):
    Z[i] = len(G[i])
    if Z[i] == 1:
        start = i
        break
else:
    print('No')
    exit()

seen = [False] * N
stack = [start]
while stack:
    v = stack.pop()
    if seen[v]:
        print('No')
        exit()
    seen[v] = True
    for w in G[v]:
        if seen[w]:
            continue
        stack.append(w)
if all(seen):
    print('Yes')
else:
    print('No')
