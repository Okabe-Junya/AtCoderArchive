def main(N, M, D, K, G, edges):
    ans = [-1] * M
    cnt = 0  # いくつ埋めたか
    p = 0  # 現在の位置
    tmp = 1  # 現在の日にち
    d = {i: 0 for i in range(N)}  # 各頂点の次数


if __name__ == "__main__":
    N, M, D, K = map(int, input().split())
    G = [[] for _ in range(N)]
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        G[u].append((v, w))
        G[v].append((u, w))
        edges.append((u, v, w))
    # 読み飛ばす
    # ビジュアライザーのための入力
    for _ in range(N):
        x, y = map(int, input().split())
    main(N, M, D, K, G, edges)
