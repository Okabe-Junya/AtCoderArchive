n = int(input())
l = list(map(int, input().split()))
a = max(l)
b = sum(l)
if a >= b - a:
    print('No')
else:
    print('Yes')
