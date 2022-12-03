N = int(input())
S = list(map(int, input().split()))
S.insert(0, 0)
k = []
for i in range(len(S) - 1):
    k.append(S[i + 1] - S[i])
print(*k)
