t = list(map(int, input().split()))
for i in range(100):
    n = int(input())
    if i % 4 == 0:
        print('L')
    elif i % 4 == 1:
        print('F')
    elif i % 4 == 2:
        print('R')
    else:
        print('B')
