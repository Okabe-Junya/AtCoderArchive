a, b = map(int, input().split())
if (a, b) == (9, 10):
    print("Yes")
    exit()
if abs((a % 10) - (b % 10)) == 1:
    print('Yes')
else:
    print('No')