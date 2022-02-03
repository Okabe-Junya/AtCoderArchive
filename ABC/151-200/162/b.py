n = int(input())
ans = 0
for i in range(n + 1):
    if i % 3 != 0 and i % 5 != 0:  # 3でも5でも割り切れなかったら足す
        ans += i  # ans = ans + i
print(ans)
