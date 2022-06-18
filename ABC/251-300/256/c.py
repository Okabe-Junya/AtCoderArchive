h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0


def judge(n):
    if 0 < n <= 28:
        return True
    else:
        return False


for i in range(1, 29):
    for j in range(1, 29):
        for k in range(1, 29):
            for l in range(1, 29):
                a13 = h1 - i - j
                a23 = h2 - k - l
                a31 = w1 - i - k
                a32 = w2 - j - l
                a33 = w3 - a13 - a23
                if a33 != h3 - a31 - a32:
                    continue
                if not judge(a13) or not judge(a23) or not judge(a31) or not judge(a32) or not judge(a33):
                    continue
                ans += 1
print(ans)
