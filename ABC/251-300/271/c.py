from collections import deque

N = int(input())
a_ = list(map(int, input().split()))
a_.sort()
a = [a_[0]]
tmp = 0
for i in range(1, N):
    if a_[i] != a_[i - 1]:
        a.append(a_[i])
    else:
        tmp += 1

a = deque(a)
ans = 0
while a:
    # print(a, tmp)
    if a[0] == ans + 1:
        ans += 1
        a.popleft()
    else:
        if tmp >= 2:
            tmp -= 2
            ans += 1
        elif tmp == 1:
            tmp = 0
            a.pop()
            ans += 1
        else:
            if len(a) >= 2:
                a.pop()
                a.pop()
                ans += 1
            else:
                if len(a) == 1 and tmp == 1:
                    ans += 1
                break
print(ans + tmp // 2)
