n = int(input())
a = list(map(int, input().split()))

cnt = [0] * 100000
for i in a:
    cnt[i] += 1
    
ans = 0
for i in range(1, 100000 // 2):
    ans += cnt[i] * cnt[100000 - i]


def comb_2(n):
    return n * (n - 1) // 2


if cnt[50000] >= 2:
    ans += comb_2(cnt[50000])
    
print(ans)