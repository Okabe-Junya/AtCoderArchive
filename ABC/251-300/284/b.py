T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in A:
        if i % 2 == 1:
            ans += 1
    print(ans)
