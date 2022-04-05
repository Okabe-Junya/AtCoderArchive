T = int(input())
for i in range(T):
    print("Case #{}:".format(i + 1))
    R, C = map(int, input().split())
    for j in range(2 * R + 1):
        if j == 0:
            print("..", end="")
            for k in range(2 * C - 1):
                if k % 2 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print()
            continue
        elif j == 1:
            print("..", end="")
            for k in range(2 * C - 1):
                if k % 2 == 0:
                    print("|", end="")
                else:
                    print(".", end="")
            print()
            continue
        elif j % 2 == 1:
            print("|", end="")
            for k in range(2 * C):
                if k % 2 == 0:
                    print(".", end="")
                else:
                    print("|", end="")
            print()
        else:
            print("+", end="")
            for k in range(2 * C):
                if k % 2 == 0:
                    print("-", end="")
                else:
                    print("+", end="")
            print()