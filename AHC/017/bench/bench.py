N, M, D, K = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append((v, w))
    G[v].append((u, w))

# 読み飛ばす
# ビジュアライザーのための入力
for _ in range(N):
    x, y = map(int, input().split())

ans = [-1] * M
for i in range(M):
    ans[i] = i // K + 1

print(*ans)
