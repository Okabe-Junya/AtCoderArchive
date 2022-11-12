N = int(input())
G = {}
for _ in range(N):
    a, b = map(int, input().split())
    if a in G:
        G[a].append(b)
    else:
        G[a] = [b]
    if b in G:
        G[b].append(a)
    else:
        G[b] = [a]

can = set()
can.add(1)
stack = [1]
while stack:
    v = stack.pop()
    if v not in G:
        continue
    for u in G[v]:
        if u not in can:
            can.add(u)
            stack.append(u)

print(max(can))
