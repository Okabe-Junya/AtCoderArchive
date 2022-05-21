N = int(input())
S = []
for i in range(N):
    S.append(list(input()))

anslist = []
for i in range(10):
    val = 0
    b = [False] * N
    while sum(b) < N:
        for k in range(N):
            if int(S[k][val % 10]) == i and (not b[k]):
                b[k] = True
                break
        val += 1
    anslist.append(val)
print(min(anslist) - 1)