from math import sqrt, floor


n = int(input())
ans = 0
l =[]
n3 = 0
while True:
    if n3 ** 3 > n:
        break
    n3 += 1

for i in range(1, n3 + 1):
    n2 = floor(sqrt(n / i))
    for j in range(i, n2 + 1):
        tmp = n // (i * j) - (j - 1)
        ans += max(0, tmp)
        #print(ans)
print(ans)