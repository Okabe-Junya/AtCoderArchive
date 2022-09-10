N = int(input())
p = list(map(int, input().split()))


dict = {}
for i in range(N):
    if (p[i] - i - 1) % N in dict:
        dict[(p[i] - i - 1) % N] += 1
    else:
        dict[(p[i] - i - 1) % N] = 1
    if (p[i] - i) % N in dict:
        dict[(p[i] - i) % N] += 1
    else:
        dict[(p[i] - i) % N] = 1
    if (p[i] - i + 1) % N in dict:
        dict[(p[i] - i + 1) % N] += 1
    else:
        dict[(p[i] - i + 1) % N] = 1
print(max(dict.values()))
