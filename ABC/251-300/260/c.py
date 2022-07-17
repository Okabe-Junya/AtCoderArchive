from collections import deque
N, X, Y = map(int, input().split())

r = deque()
b = deque()

r.append((N, 1))
ans = 0

def red(r, b):
    n, num = r.popleft()
    if n == 1:
        return r, b
    r.append((n-1, num))
    b.append((n, num * X))
    return r, b
    

def blue(r, b, ans):
    n, num = b.popleft()
    if n == 1:
        ans += num
        return r, b, ans
    r.append((n-1, num))
    b.append((n-1, num * Y))
    return r, b, ans

while r or b:
    if r:
        r, b = red(r, b)
    if b:
        r, b, ans = blue(r, b, ans)
print(ans)