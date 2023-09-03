from collections import deque

N = int(input())
parents = list(map(int, input().split()))

G = [set() for _ in range(N)]
for i in range(N - 1):
    a = parents[i] - 1
    b = i + 1
    G[a].add(b)
    G[b].add(a)


def f(x):
    E = deque()
    E.append(x)
    S = set()
    Sl = []
    while E:
        y = E.popleft()
        C = G[y] - S
        C = list(C)
        C.sort(reverse=True)
        for c in C:
            E.appendleft(c)
        S.add(y)
        Sl.append(y)

    return Sl[-1]


ans = []
for i in range(N):
    ans.append(f(i) + 1)
print(*ans)
