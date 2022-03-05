import math
n, k = map(int, input().split())
a = list(map(int, input().split()))
i = a.index(1)
print(math.ceil((n - 1) / (k - 1)))
