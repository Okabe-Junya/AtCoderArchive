n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = -max(x) + min(y) + 1
if a > 0:
    print(a)
else:
    print(0)
