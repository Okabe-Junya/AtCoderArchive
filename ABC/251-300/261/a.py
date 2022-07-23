L1, R1, L2, R2 = map(int, input().split())

X = [0] * 101
for i in range(L1, R1):
    X[i] += 1

for i in range(L2, R2):
    X[i] += 1

ans = 0
for i in range(101):
    if X[i] == 2:
        ans += 1

print(ans)