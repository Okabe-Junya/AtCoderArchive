def d(s):
    return len(list(str(s)))


a, b, x = map(int, input().split())


def bin_search():
    INF = 10 ** 9
    if a * INF + b * d(INF) <= x:
        return INF

    pl = 0
    pr = INF
    while True:
        pc = (pl + pr) // 2
        if x-1 < a * pc + b * d(pc) <= x:
            return pc
        elif a * pc + b * d(pc) > x:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    while pr > 0:
        if a * pr + b * d(pr) <= x:
            return pr
        pr -= 1
    return 0


print(bin_search())
