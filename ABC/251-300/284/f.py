from collections import deque

N = int(input())
T = input()
start = deque()
for i in range(N):
    start.append(T[2 * N - 1 - i])

print(start)

dict = {2 * N - 1: start}
for i in range(2 * N - 2, N - 1, -1):
    start.popleft()
    start.append(T[i])
    dict[i] = start

print(dict)
