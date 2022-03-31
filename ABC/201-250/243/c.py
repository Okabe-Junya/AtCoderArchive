N = int(input())
X = []; Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
S = input()
L = {}
R = {}

for i in range(N):
    if S[i] == 'L':
        if R[Y[i]] < X[i]:
            print("Yes")
            exit()
        