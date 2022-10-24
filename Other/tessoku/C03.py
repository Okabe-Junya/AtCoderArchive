D = int(input())
X = int(input())
L = [X]
for _ in range(D - 1):
    A = int(input())
    L.append(A + L[-1])

for _ in range(int(input())):
    S, T = map(int, input().split())
    if L[S - 1] > L[T - 1]:
        print(S)
    elif L[S - 1] < L[T - 1]:
        print(T)
    else:
        print('Same')
