N = int(input())
A = list(map(int, input().split()))
Asum = [A[0]]
for i in range(1, N):
    Asum.append(Asum[i - 1] + A[i])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    all = R - L + 1
    if L != 1:
        one = Asum[R - 1] - Asum[L - 2]
    else:
        one = Asum[R - 1]
    zero = all - one
    if one > zero:
        print('win')
    elif one < zero:
        print('lose')
    else:
        print('draw')
