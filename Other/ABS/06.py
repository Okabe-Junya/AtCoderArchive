n, a, b = map(int, input().split())
idx = 0
for i in range(1, n+1):
    if a <= sum([int(c) for c in str(i)]) <= b:
        idx += i
print(idx)
