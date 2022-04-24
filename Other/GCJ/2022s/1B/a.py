def case(i):
    print("Case #{}:".format(i), end=" ")

from collections import deque

T = int(input())
for i in range(T):
    N = int(input())
    D = deque(map(int, input().split()))
    case(i + 1)
    tmp = 0
    ans = 0
    for _ in range(len(D)):
        n = min(D[0], D[-1])
        if n >= tmp:
            ans += 1
            tmp = n
            if tmp == D[0]:
                D.popleft()
            else:
                D.pop()
        else:
            if D[0] > D[-1]:
                if D[0] >= tmp:
                    ans += 1
                    tmp = D[0]
                    D.popleft()
                else:
                    break
            else:
                if D[-1] >= tmp:
                    ans += 1
                    tmp = D[-1]
                    D.pop()
                else:
                    break
    print(ans)