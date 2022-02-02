t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print('Same')
    elif n % 2 == 1:
        print('Odd')
    else:
        if n % 4 == 0:
            print('Even')
        else:
            print('Same')
