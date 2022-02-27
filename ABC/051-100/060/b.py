a, b, c = map(int, input().split())
for i in range(b):
    if (a * (i + 1)) % b == c:
        print('YES')
        break
else:
    print('NO')
