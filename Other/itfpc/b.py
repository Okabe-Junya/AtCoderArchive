N, X = map(int, input().split())
L = []
for _ in range(N):
    A, S = map(int, input().split())
    L.append((A, S))

L.sort(key=lambda x: x[0])
for i in range(N - 1):
    if L[i][1] > L[i + 1][1]:
        print("Dangerous")
        exit()
for i in range(N):
    if L[i][1] > X:
        print("Over")
        exit()
print("Safe")
