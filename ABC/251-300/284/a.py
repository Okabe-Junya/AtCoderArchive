N = int(input())
Sl = []
for i in range(N):
    S = input()
    Sl.append(S)

for i in range(N):
    print(Sl[N - i - 1])
