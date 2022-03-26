N = int(input())
A = list(map(int, input().split()))
S = set(A)
for i in range(2001):
    if i not in S:
        print(i)
        exit()
else:
    print(2001)