while True:
    n = int(input())
    if n == 0:
        break
    L = []
    for _ in range(n):
        s = int(input())
        L.append(s)
    L.sort()
    L.pop(0)
    L.pop()
    print(int(sum(L) / len(L)))