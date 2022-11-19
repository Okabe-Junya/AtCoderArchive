H, M = map(int, input().split())


def is_mimachi(A, B, C, D):
    if 0 <= int(str(A) + str(C)) <= 23 and 0 <= int(str(B) + str(D)) <= 59:
        return True
    return False


while True:
    A, B, C, D = str(H // 10), str(H % 10), str(M // 10), str(M % 10)
    if is_mimachi(A, B, C, D):
        print(A + B + " " + C + D)
        exit()

    if H == 23 and M == 59:
        H, M = 0, 0
    elif M == 59:
        H += 1
        M = 0
    else:
        M += 1
