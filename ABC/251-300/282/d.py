N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)

colors = []
seen = [False] * N
for i in range(N):
    if seen[i]:
        continue
    color = {0: set([i]), 1: set()}
    stack = [(i, 0)]
    while stack:
        v, c = stack.pop()
        seen[v] = True
        for w in G[v]:
            if w in color[c]:
                print(0)
                exit()
            if w not in color[1 - c]:
                color[1 - c].add(w)
                stack.append((w, 1 - c))
    colors.append(color)

ans = 0
for i in range(len(colors)):
    ans += len(colors[i][0]) * len(colors[i][1])
len_list = []
for i in range(len(colors)):
    len_list.append(len(colors[i][0]) + len(colors[i][1]))
sum_list = [len_list[-1]]
for i in range(1, len(len_list)):
    sum_list.append(sum_list[-1] + len_list[-i - 1])
for i in range(len(sum_list) - 1):
    ans += sum_list[i] * len_list[len(len_list) - i - 2]

print(ans - M)
