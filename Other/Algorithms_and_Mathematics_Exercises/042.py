N = int(input())
ans = 0
for i in range(1, N + 1):
    tmp_max = N // i
    ans += (tmp_max * (tmp_max + 1) // 2) * i
print(ans)