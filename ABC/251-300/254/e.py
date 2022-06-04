from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    seen = {}
    ans = x
    queue = deque([x - 1])
    seen[x - 1] = 0
    while queue:
        next = queue.popleft()
        for i in G[next]:
            if i not in seen:
                seen[i] = seen[next] + 1
                if seen[i] <= k:
                    ans += i + 1
                    if seen[i] < k:
                        queue.append(i)
    print(ans)