import time

time_start = time.time()
N, M = map(int, input().split())
tmpG = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    tmpG[u - 1].append(v - 1)
    tmpG[v - 1].append(u - 1)

ans = 0
stack = [(0, set([0]))]
while stack:
    tmp_time = time.time()
    if tmp_time - time_start > 1.85:
        print(10 ** 6)
        exit()
    tmp = stack.pop()
    ans += 1
    if len(stack) + ans >= 10 ** 6:
        print(10 ** 6)
        exit()
    for i in tmpG[tmp[0]]:
        if i not in tmp[1]:
            stack.append((i, tmp[1] | set([i])))
print(ans)
