N = int(input())

E = [0 for _ in range(N + 1)]
E[1] = 3.5
for i in range(2, N + 1):
    E[i] = 6 - E[i - 1] / i
print(E[-1])
