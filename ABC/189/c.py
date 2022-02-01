n = int(input())
a = list(map(int, input().split()))
ans = min(a) * n
b = set(a)
c = sorted(b)
c.pop(0)
for i in c:
    cnt = 0
    l = []
    for j in a:
        if j >= i:
            cnt += 1
        else:
            l.append(cnt)
            cnt = 0
    if a[-1] >= i:
        d = 1
        while True:
            if not a[(-1 * d)] >= i:
                break
            d += 1
        l.append(d-1)

    ans_n = max(l) * i
    if ans < ans_n:
        ans = ans_n
print(ans)
