N = int(input())
seen = [False] * N
start = []
goal = []
sx, sy, tx, ty = map(int, input().split())
L = []
G = [[] for i in range(N)]
for i in range(N):
    L.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1, N):
        if (L[i][2] - L[j][2]) ** 2 <= ((L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2) <= (L[i][2] + L[j][2]) ** 2:
            G[i].append(j)
            G[j].append(i)

for i in range(N):
    if (sx - L[i][0]) ** 2 + (sy - L[i][1]) ** 2 == L[i][2] ** 2:
        start.append(i)
    if (tx - L[i][0]) ** 2 + (ty - L[i][1]) ** 2 == L[i][2] ** 2:
        goal.append(i)


goal_set = set(goal)

for st in start:
    if seen[st]:
        continue
    seen[st] = True
    stack = [st]
    while stack:
        v = stack.pop()
        for w in G[v]:
            if seen[w]:
                continue
            seen[w] = True
            stack.append(w)
            if w in goal_set:
                print('Yes')
                exit()

for go in goal:
    if seen[go]:
        print('Yes')
        break
else:
    print('No')