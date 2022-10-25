N = int(input())
X = 0
for _ in range(N):
    T, A = input().split()
    if T == '+':
        X += int(A)
    elif T == '-':
        X -= int(A)
    elif T == '*':
        X *= int(A)
    X %= 10000
    print(X)
