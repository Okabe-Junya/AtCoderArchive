H, W = map(int, input().split())
L = [list(input()) for _ in range(H)]
ans = [[0] * W for _ in range(H)]
ans[0][0] = 1
for i in range(H):
    for j in range(W):
        if i == j == 0:
            continue
        if i >= 1 and L[i - 1][j] == ".":
            ans[i][j] += ans[i - 1][j]
        if j >= 1 and L[i][j - 1] == ".":
            ans[i][j] += ans[i][j - 1]

print(ans[-1][-1])
