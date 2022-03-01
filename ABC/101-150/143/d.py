from itertools import combinations as cmb

N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
L_cnt = [0] * (1001)
L_cnt_sum = [0] * (1001)
for i in L:
    L_cnt[i] += 1

for i in range(1, 1001):
    L_cnt_sum[i] = L_cnt_sum[i - 1] + L_cnt[i]

# print(L_cnt_sum[:10])
l = cmb(L, 2)
for i in l:
    # print(i)
    Sum = sum(i)
    ans += max(0, L_cnt_sum[Sum - 1] - L_cnt_sum[i[1] - i[0] + 1])
    print(ans)
print(ans // 6)