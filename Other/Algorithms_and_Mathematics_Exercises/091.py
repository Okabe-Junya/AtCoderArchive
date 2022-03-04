N, X = map(int, input().split())
ans = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if i + j + k == X:
                # print(i, j, k)
                ans += 1
print(ans)