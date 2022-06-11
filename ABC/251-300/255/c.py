X, A, D, N = map(int, input().split())
start = A
last = A + D * (N - 1)
if not((start <= X <= last) or (start >= X >= last)):
    print(min(abs(start - X), abs(last - X)))
else:
    if D == 0:
        print(abs(X - A))
        exit()
    K = (X - A) // D
    print(min(abs(X - A - K * D), abs(X - A - (K + 1) * D), abs(X - A - (K - 1) * D)))
