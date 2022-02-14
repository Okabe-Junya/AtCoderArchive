n, q = map(int, input().split())
a = list(map(int, input().split()))
b = []
ans = 0
for i in a:
    ans ^= i
    b.append(ans)

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        ans ^= a[x - 1]
        ans ^= a[y - 1]
    else:
        print(ans)