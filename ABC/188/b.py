n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
cnt = 0
for i in range(len(x)):
    cnt += x[i] * y[i]
if cnt == 0:
    print('Yes')
else:
    print('No')
