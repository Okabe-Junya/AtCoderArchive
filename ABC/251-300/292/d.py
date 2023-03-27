N, M = map(int, input().split())
G = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    G2[a - 1].append(b - 1)

seen = [-1] * N
cnt = 0
group = []
for i in range(N):
    tmp = []
    cnt += 1
    if seen[i] != -1:
        continue
    seen[i] = cnt
    stack = [i]
    tmp.append(i)
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if seen[nv] == -1:
                seen[nv] = cnt
                stack.append(nv)
                tmp.append(nv)
    group.append(tmp)
for g in group:
    esum = 0
    for v in g:
        esum += len(G2[v])
    if esum != len(g):
        print("No")
        exit()
print("Yes")
