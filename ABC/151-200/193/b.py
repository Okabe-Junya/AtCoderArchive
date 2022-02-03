n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
ans = 10 ** 9 + 1
for b in a:
    if b[2] - b[0] > 0:
        if ans > b[1]:
            ans = b[1]
if ans == 10 ** 9 + 1:
    print(-1)
else:
    print(ans)
