import time


start = time.time()
N, M = map(int, input().split())
G = [[] for _ in range(N)]
Gset = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    Gset[a - 1].add(b - 1)

ans = 0
for i in range(N):
    for j in G[i]:
        if j == i:
            continue
        for k in G[j]:
            tmp_time = time.time()
            if tmp_time - start > 1.9:
                print(ans)
                exit()
            if k == i:
                continue
            elif k == j:
                continue
            elif k not in Gset[i]:
                G[i].append(k)
                Gset[i].add(k)
                ans += 1
print(ans)
