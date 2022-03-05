def hantei2(b, c):
    if b % 4 == 0:
        return 0
    elif b % 4 == 1:
        return 1
    elif b % 4 == 2:
        if c == 1:
            return 2
        else:
            return 0
    elif b % 4 == 3:
        if c % 2 == 1:
            return 3
        else:
            return 1
# n ** b の一の位


def hantei(n, b):
    if n % 10 == 0:
        return 10

    elif n % 10 == 1:
        return 1

    elif n % 10 == 2:
        if b % 4 == 1:
            return 2
        elif b % 4 == 2:
            return 4
        elif b % 4 == 3:
            return 8
        elif b % 4 == 0:
            return 6

    elif n % 10 == 3:
        if b % 4 == 1:
            return 3
        elif b % 4 == 2:
            return 9
        elif b % 4 == 3:
            return 7
        elif b % 4 == 0:
            return 1

    elif n % 10 == 4:
        if b % 2 == 1:
            return 4
        else:
            return 6

    elif n % 10 == 5:
        return 5

    elif n % 10 == 6:
        return 6

    elif n % 10 == 7:
        if b % 4 == 1:
            return 7
        elif b % 4 == 2:
            return 9
        elif b % 4 == 3:
            return 3
        elif b % 4 == 0:
            return 1

    elif n % 10 == 8:
        if b % 4 == 1:
            return 8
        elif b % 4 == 2:
            return 4
        elif b % 4 == 3:
            return 2
        elif b % 4 == 0:
            return 6

    elif n % 10 == 9:
        if b % 2 == 1:
            return 9
        else:
            return 1


a, b, c = map(int, input().split())
d = a % 10
ans_1 = hantei2(b, c)
ans = hantei(a, ans_1)
print(ans % 10)
