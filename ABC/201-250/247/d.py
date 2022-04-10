from collections import deque


Q = int(input())
L = deque()
for _ in range(Q):
    s = input().split()
    if s[0] == "1":
        if len(L) > 0:
            if L[-1][0] == int(s[1]):
                L[-1][1] += int(s[2])
            else:
                L.append([int(s[1]), int(s[2])])
        else:
            L.append([int(s[1]), int(s[2])])
    else:
        ans = 0
        cnt = int(s[1])
        for i in range(len(L)):
            tmp = L[0]
            if tmp[1] < cnt:
                cnt -= tmp[1]
                ans += tmp[0] * tmp[1]
                L.popleft()
            else:
                ans += tmp[0] * cnt
                L[0][1] -= cnt
                break
        print(ans)
