n, k = map(int, input().split())

if k % 2 == 0:
    num = n // k
    ans = num ** 3
    num = (n - k // 2) // k + 1
    ans += num ** 3
    print(ans)
else:
    num = n // k
    print(num ** 3)