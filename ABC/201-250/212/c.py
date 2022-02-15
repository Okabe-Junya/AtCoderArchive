import bisect


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.sort()
ans = 10 ** 9
for i in range(n):
    res = bisect.bisect_left(b, a[i])
    # print(res)
    if res == m:
        res -= 1
    tmp = min(abs(a[i] - b[res]), abs(a[i] - b[res - 1]))
    if ans > tmp:
        ans = tmp
print(ans)