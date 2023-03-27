from collections import deque


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    C = input().split()
    for i in range(N):
        C[i] = int(C[i])
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    if C[0] == C[-1]:
        print(-1)
        continue

    seen = set()
    seen.add((0, N - 1))
    q = deque()
    q.append((0, N - 1, 0))
    while q:
        # print(q)
        tmp_t, tmp_a, num = q.popleft()
        if tmp_t == N - 1 and tmp_a == 0:
            print(num)
            break
        for i in G[tmp_t]:
            for j in G[tmp_a]:
                if C[i] + C[j] == 1 and (i, j) not in seen:
                    q.append((i, j, num + 1))
                    seen.add((i, j))
    else:
        print(-1)
