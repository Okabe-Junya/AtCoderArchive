from collections import deque

N = int(input())
G = {}
L = []
all = set()
for _ in range(N):
    S, T = input().split()
    G[S] = T
    L.append((S, T))
    all.add(S)
    all.add(T)

# サイクル検出
deg = {}
for _, t in L:
    if t not in deg:
        deg[t] = 0
    deg[t] += 1

queue = deque()
for s, _ in L:
    if s not in deg:
        queue.append(s)

order = []
while queue:
    s = queue.popleft()
    order.append(s)
    if s in G:
        t = G[s]
        deg[t] -= 1
        if deg[t] == 0:
            queue.append(t)

if len(order) == len(all):
    print("Yes")
else:
    print("No")
