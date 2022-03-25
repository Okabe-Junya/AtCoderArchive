N = int(input())
L = set(range(1, 2 * N + 2))

while True:
    own = list(L)[0]
    L.discard(own)
    print(own)
    tmp = int(input())
    if tmp == 0:
        break
    L.discard(tmp)
exit()