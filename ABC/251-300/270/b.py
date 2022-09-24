X, Y, Z = map(int, input().split())
if (0 < Y < X) or (0 > Y > X):
    if (Z > Y > 0) or (Z < Y < 0):
        print(-1)
    else:
        print(abs(Z) + abs(Z - X))
else:
    print(abs(X))
