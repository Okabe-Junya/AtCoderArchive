N, M = map(int, input().split())
lamps = [list(map(lambda x:int(x)-1, input().split()))[1:]
         for _ in range(M)]
p = list(map(int, input().split()))
ans = 0

for i in range(2 ** N):
    for r in range(M):
        on_sum = 0
        for j in range(N):
            if i >> j & 1 and j in lamps[r]:
                on_sum += 1
        if on_sum % 2 != p[r]:
            break
    else:
        ans += 1
print(ans)
