T = int(input())
for i in range(T):
    print("Case #{}:".format(i + 1), end=" ")
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    p = 0
    for i in range(N):
        if L[i] >= p + 1:
            ans += 1
            p += 1
    print(ans)