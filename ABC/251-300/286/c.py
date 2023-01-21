from collections import deque

N, A, B = map(int, input().split())
S = list(input())
S = deque(S)
ans = float("inf")
for i in range(N):
    # print(S)
    cnt = 0
    for j in range(N // 2):
        if S[j] != S[-j - 1]:
            cnt += 1
    if i * A + cnt * B < ans:
        ans = i * A + cnt * B

    n = S.popleft()
    S.append(n)
print(ans)
