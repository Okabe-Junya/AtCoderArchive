from typing import List


class RMQ(object):
    def __init__(self, L: List[int]):
        self.tree = [0] * (300_000 + 1)  # 1-indexed
        self.size = 1
        while self.size < len(L):
            self.size *= 2
        for i in range(1, self.size + 1):
            self.tree[i] = 0

    def _update(self, pos: int, x: int) -> None:
        """tree[pos] の値を x にする"""
        pos += self.size - 1
        self.tree[pos] = x
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[pos * 2], self.tree[pos * 2 + 1])

    def _query(self, a: int, b: int, k: int, left: int, right: int) -> int:
        """[a, b) の最大値を求める"""
        if right <= a or b <= left:
            return 0
        if left <= a and b <= right:
            return self.tree[k]
        m = (a + b) // 2
        al = self._query(a, m, k * 2, left, right)
        ar = self._query(m, b, k * 2 + 1, left, right)
        return max(al, ar)


N, Q = map(int, input().split())
rmq = RMQ([0] * N)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        pos, x = q[1:]
        rmq._update(pos, x)
    elif q[0] == 2:
        l, r = q[1:]
        print(rmq._query(1, rmq.size + 1, 1, l, r))
