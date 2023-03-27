N, M, D, K = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append((v, w, i))  # (行き先, 重み, 辺の番号)
    G[v].append((u, w, i))  # (行き先, 重み, 辺の番号)

# 読み飛ばす
# ビジュアライザーのための入力
for _ in range(N):
    x, y = map(int, input().split())

ans = [-1] * M
tmp = 0
for i in range(M):
    ans[i] = tmp + 1
    tmp += 1
    tmp %= D

print(*ans)
