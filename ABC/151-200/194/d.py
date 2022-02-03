n = int(input())
e = 0
for k in range(1, n):
    e += (n/(n-k))
print(e)
