def solve(s, t):
    s_score = 0
    t_score = 0
    for i in range(1, 10):
        tmp_s = 0
        tmp_t = 0
        for m in s:
            if m == str(i):
                tmp_s += 1
        for n in t:
            if n == str(i):
                tmp_t += 1
        s_score += i * (10 ** tmp_s)
        t_score += i * (10 ** tmp_t)
    if s_score > t_score:
        return True
    else:
        return False


k = int(input())
s = list(input())
t = list(input())
s[-1] = '0'
t[-1] = '0'
a = [[False for _ in range(10)] for _ in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        s[-1] = str(i)
        t[-1] = str(j)
        b = True
        for c in range(1, 10):
            if s.count(str(c)) + t.count(str(c)) > k:
                b = False
                a[i][j] = -1
                break
        if b:
            if solve(s, t):
                a[i][j] = True
ans = 0
al = 0
for i in range(1, 10):
    for j in range(1, 10):
        s[-1] = 0
        t[-1] = 0
        if a[i][j] == -1:
            continue
        elif a[i][j] and i == j:
            n = s.count(str(i)) + t.count(str(j))
            tmp = (k-n) * (k-n-1)
            ans += tmp
            al += tmp
        elif i == j:
            n = s.count(str(i)) + t.count(str(j))
            al += (k-n) * (k-n-1)
        else:
            tmp = (k - s.count(str(i))-t.count(str(i))) * \
                (k - t.count(str(j))-s.count(str(j)))
            al += tmp
            if a[i][j]:
                ans += tmp
print(ans/al)
