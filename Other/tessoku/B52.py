from collections import deque

N, X = map(int, input().split())
A = list(input())
queue = deque([X - 1])
A[X - 1] = "@"
while queue:
    next = queue.popleft()
    if next - 1 >= 0:
        if A[next - 1] == ".":
            queue.append(next - 1)
            A[next - 1] = "@"
    if next + 1 < N:
        if A[next + 1] == ".":
            queue.append(next + 1)
            A[next + 1] = "@"
print("".join(A))
