import argparse
import sys
from copy import deepcopy
from random import choice


class Box:
    def __init__(self, f, debug=False) -> None:
        self.box = [[0] * 10 for _ in range(10)]
        self.f = f
        self.debug = False
        if debug:
            self.debug = True

    def step(self, fi, pi=-1):
        if pi == -1:
            pi = int(input())
        x, y = self.search_empty(pi)
        self.box[x][y] = fi

    def search_empty(self, pi):
        cnt = 0
        for i in range(10):
            for j in range(10):
                if self.box[i][j] == 0:
                    cnt += 1
                    if cnt >= pi:
                        return i, j

    def solve(self):
        dict = {0: "L", 1: "R", 2: "F", 3: "B"}
        for i in range(98):
            res = []
            self.step(self.f[i])

            nx = [deepcopy(self), deepcopy(self), deepcopy(self), deepcopy(self)]
            for idx in range(4):
                if idx == 0:
                    nx[idx].left()
                elif idx == 1:
                    nx[idx].right()
                elif idx == 2:
                    nx[idx].front()
                else:
                    nx[idx].back()
                nnx = [
                    deepcopy(nx[idx]),
                    deepcopy(nx[idx]),
                    deepcopy(nx[idx]),
                    deepcopy(nx[idx]),
                ]
                nnx_res = []
                for iidx in range(4):
                    nnx[iidx].step(self.f[i + 1], (100 - i) // 2)
                    if iidx == 0:
                        nnx[iidx].left()
                    elif iidx == 1:
                        nnx[iidx].right()
                    elif iidx == 2:
                        nnx[iidx].front()
                    else:
                        nnx[iidx].back()
                    nnnx = [
                        deepcopy(nnx[iidx]),
                        deepcopy(nnx[iidx]),
                        deepcopy(nnx[iidx]),
                        deepcopy(nnx[iidx]),
                    ]
                    nnnx_res = []
                    for iiidx in range(4):
                        nnnx[iiidx].step(self.f[i + 2], (100 - i) // 2)
                        if iiidx == 0:
                            nnnx[iiidx].left()
                        elif iiidx == 1:
                            nnnx[iiidx].right()
                        elif iiidx == 2:
                            nnnx[iiidx].front()
                        else:
                            nnnx[iiidx].back()
                        nnnx_res.append(nnnx[iiidx].score())
                    nnx_res.append(max(nnnx_res))

                res.append(max(nnx_res))

            nextd = res.index(max(res))
            didx = []
            for idx in range(4):
                if res[idx] == res[nextd]:
                    didx.append(idx)

            nextd = choice(didx)
            if i == 50:
                if self.debug:
                    print("=== 50回目終了時点 ===", file=sys.stderr)
                    print(self.box, file=sys.stderr)
                    print(res, file=sys.stderr)

            if nextd == 0:
                self.left()
            elif nextd == 1:
                self.right()
            elif nextd == 2:
                self.front()
            else:
                self.back()

            if not self.debug:
                print(dict[nextd])
        nx = [deepcopy(self), deepcopy(self), deepcopy(self), deepcopy(self)]
        res = []
        for idx in range(4):
            if idx == 0:
                nx[idx].left()
            elif idx == 1:
                nx[idx].right()
            elif idx == 2:
                nx[idx].front()
            else:
                nx[idx].back()
            nnx = [
                deepcopy(nx[idx]),
                deepcopy(nx[idx]),
                deepcopy(nx[idx]),
                deepcopy(nx[idx]),
            ]
            nnx_res = []
            for iidx in range(4):
                nnx[iidx].step(self.f[i + 1], 1)
                if iidx == 0:
                    nnx[iidx].left()
                elif iidx == 1:
                    nnx[iidx].right()
                elif iidx == 2:
                    nnx[iidx].front()
                else:
                    nnx[iidx].back()
                nnx_res.append(nnx[iidx].score())
            res.append(max(nnx_res))
        nextd = res.index(max(res))
        if not self.debug:
            print(dict[nextd])
            print("L")
        else:
            print("=== result ===", file=sys.stderr)
            print(self.box, file=sys.stderr)
            print("=== score ===", file=sys.stderr)
            print(self.score(), file=sys.stderr)

    def left(self):
        for i in range(10):
            tmp = []
            cnt = 0
            for j in range(10):
                if self.box[i][j] != 0:
                    tmp.append(self.box[i][j])
                else:
                    cnt += 1
            for _ in range(cnt):
                tmp.append(0)
            self.box[i] = tmp
        return self

    def right(self):
        for i in range(10):
            tmp = []
            cnt = 0
            for j in range(10):
                if self.box[i][j] != 0:
                    tmp.append(self.box[i][j])
                else:
                    cnt += 1
            for _ in range(cnt):
                tmp.insert(0, 0)
            self.box[i] = tmp

    def front(self):
        for j in range(10):
            tmp = []
            for i in range(10):
                tmp.append(self.box[i][j])
            res = []
            cnt = 0
            for i in range(10):
                if tmp[i] != 0:
                    res.append(tmp[i])
                else:
                    cnt += 1
            for _ in range(cnt):
                res.append(0)
            for i in range(10):
                self.box[i][j] = res[i]

    def back(self):
        for j in range(10):
            tmp = []
            for i in range(10):
                tmp.append(self.box[i][j])
            res = []
            cnt = 0
            for i in range(10):
                if tmp[i] != 0:
                    res.append(tmp[i])
                else:
                    cnt += 1
            for _ in range(cnt):
                res.insert(0, 0)
            for i in range(10):
                self.box[i][j] = res[i]

    def score(self):
        con = [0]
        d = ((0, 1), (1, 0), (0, -1), (-1, 0))
        seen = [[-1] * 10 for _ in range(10)]
        for i in range(10):
            for j in range(10):
                if seen[i][j] != -1:
                    continue
                if self.box[i][j] == 0:
                    continue
                tmp_con = 0
                stack = [(i, j)]
                same = self.box[i][j]
                while stack:
                    x, y = stack.pop()
                    if seen[x][y] != -1:
                        continue
                    seen[x][y] = same
                    tmp_con += 1
                    for dx, dy in d:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 10 and 0 <= ny < 10 and self.box[nx][ny] == same:
                            stack.append((nx, ny))
                con.append(tmp_con)
        retval = 0
        for val in con:
            retval += val**2
        return retval


def main():
    # --debug でデバッグモード
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")

    f = list(map(int, input().split()))
    box = Box(f, debug=parser.parse_args().debug)
    box.solve()


if __name__ == "__main__":
    main()
