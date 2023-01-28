N = int(input())
L = []
for _ in range(N):
    L.append(input())

if L.count('For') > L.count('Against'):
    print('Yes')
else:
    print('No')
