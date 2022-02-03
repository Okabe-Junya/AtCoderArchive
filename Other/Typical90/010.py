n = int(input())
in_a = [0 for _ in range(n+1)]
in_b = [0 for _ in range(n+1)]
for i in range(n):
    c, p = map(int,input().split())
    if c == 1:
        in_a[i+1] = p
    else:
        in_b[i+1] = p
a = [0]
b = [0]
for i in range(n+1):
    a.append(a[-1] + in_a[i])
    b.append(b[-1] + in_b[i])
q = int(input())
for _ in range(q):
    l, r = map(int,input().split())
    print((a[r+1] - a[l]),(b[r+1] - b[l]))