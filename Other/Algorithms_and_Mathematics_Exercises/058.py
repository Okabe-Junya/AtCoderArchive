N, X, Y = map(int, input().split())
cnt = N - abs(X) - abs(Y)
if cnt >= 0 and cnt % 2 == 0:
    print("Yes")
else:
    print("No")