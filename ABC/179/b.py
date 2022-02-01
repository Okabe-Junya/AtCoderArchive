n = int(input())
tmp = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        tmp += 1
    else:
        tmp = 0
    if tmp == 3:
        print('Yes')
        break
else:
    print('No')
