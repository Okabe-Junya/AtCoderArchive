n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
if ((k - s) >= 0) & ((k - s) % 2 == 0):
    print("Yes")
else:
    print("No")