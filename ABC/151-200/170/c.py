x, n = map(int, input().split())
p = list(map(int, input().split()))
for i in range(100):
    tmp = x - i
    if tmp not in p:
        print(tmp)
        break
    tmp = x + i
    if tmp not in p:
        print(tmp)
        break
    tmp = x
