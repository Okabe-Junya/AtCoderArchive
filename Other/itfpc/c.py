T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = [0] * 4
    for i in range(N):
        cnt[A[i] % 4] += B[i]
    ans = cnt[0]
    cnt[0] = 0
    if cnt[1] > cnt[3]:
        ans += cnt[3]
        cnt[1] -= cnt[3]
        cnt[3] = 0
        ans += cnt[1] // 4
        cnt[1] %= 4
        if cnt[1] >= 2:
            cnt[2] += 1
            cnt[1] -= 2
    else:
        ans += cnt[1]
        cnt[3] -= cnt[1]
        cnt[1] = 0
        ans += cnt[3] // 4
        cnt[3] %= 4
        if cnt[3] >= 2:
            cnt[2] += 1
            cnt[3] -= 2
    ans += cnt[2] // 2
    cnt[2] %= 2
    print(ans)
