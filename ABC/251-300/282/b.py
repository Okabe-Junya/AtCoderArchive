N, M = map(int, input().split())
ans = 0
S = [input() for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        cnt = 0
        for k in range(M):
            if S[i][k] == 'o' or S[j][k] == 'o':
                cnt += 1
        if cnt == M:
            ans += 1
print(ans)
