N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

prev = [-1] * N
seen = [False] * N


stack = [X - 1]
while stack:
    v = stack.pop()
    if seen[v]:
        continue
    seen[v] = True
    for u in G[v]:
        if not seen[u]:
            prev[u] = v
            stack.append(u)


ans = [Y - 1]
while True:
    v = prev[ans[-1]]
    if v == -1:
        break
    ans.append(v)

ans.reverse()
for i in ans:
    print(i + 1, end=' ')
print()
