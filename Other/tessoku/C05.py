N = int(input())
tmp = str(bin(N - 1)[2:]).zfill(10)
for i in tmp:
    if i == '0':
        print('4', end='')
    else:
        print('7', end='')
print()
