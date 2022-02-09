n = int(input())
a = list(map(int, input().split()))
cnt = [0] * 3
for i in a:
    cnt[i - 1] += 1


def comb_2(n):
    return n * (n - 1) // 2


ans = 0
for num in cnt:
    if num >= 2:
        ans += comb_2(num)

print(ans)