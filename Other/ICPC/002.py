while True:
    n = int(input())
    if  n == 0:
        break
    d = list(map(int, input().split()))
    ans = 0
    for i in range(n - 3):
        if d[i] == 2 and d[i + 1] == 0 and d[i + 2] == 2 and d[i + 3] == 0:
            ans += 1
    print(ans)