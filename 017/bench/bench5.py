N, M, D, K = map(int, input().split())
edges = []
for m in range(M):
    _, _, w = map(int, input().split())
    edges.append((w, m))

edges.sort()

# 読み飛ばす
# ビジュアライザーのための入力
for _ in range(N):
    x, y = map(int, input().split())

ans = [-1] * M
cnt = 0
for edge in edges:
    ans[edge[1]] = cnt // K + 1
    cnt += 1
print(*ans)
