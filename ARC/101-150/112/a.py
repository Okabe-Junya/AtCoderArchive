t = int(input())
for _ in range(t):
    cnt = 0
    l, r = map(int, input().split())
    if r < 2 * l:
        print(0)
    else:
        cnt = (r + 1 - 2 * l) * (r + 2 - 2 * l) // 2
        print(cnt)
