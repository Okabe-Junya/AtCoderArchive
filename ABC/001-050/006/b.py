n = int(input())
dp = [0, 0, 1]
for i in range(n):
    dp.append((dp[-1] + dp[-2] + dp[-3]) % 10007)
print(dp[-4])
