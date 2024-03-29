from typing import List

N = int(input())
times = []
for _ in range(N):
    L, R = map(int, input().split())
    times.append((L, R))


def schedule(times: List[List[int]]) -> int:
    """区間スケジューリング問題の最大値を求める"""
    times.sort(key=lambda x: x[1])
    ans = 0
    tmp = 0
    for i in range(len(times)):
        if tmp <= times[i][0]:  # 境界は重なってもよい（ダメなら < ）
            ans += 1
            tmp = times[i][1]
    return ans


print(schedule(times))
