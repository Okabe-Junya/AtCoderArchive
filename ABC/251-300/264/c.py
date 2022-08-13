H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]

H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

Bidx = [-1] * W2

for i in range(H1):
    p = 0
    for j in range(W1):
        if A[i][j] == B[0][p]:
            Bidx[p] = j
            p += 1
            if p == W2:
                break
    if p == W2:
        break
else:
    print("No")
    exit()

if H2 == 1:
    print("Yes")
    exit()
p = 1
while i < H1 and p < H2:
    for j in range(W2):
        if A[i][Bidx[j]] != B[p][j]:
            break
    else:
        p += 1
    if p == H2:
        print("Yes")
        exit()
    i += 1
print("No")
