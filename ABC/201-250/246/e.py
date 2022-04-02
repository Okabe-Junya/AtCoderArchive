N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
S = []
for _ in range(N):
    Si = input()
    S.append(list(Si))
if ((Ax + Ay) % 2) != ((Bx + By) % 2):
    print(-1)
    exit()

d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
seen =[[False for _ in range(N)] for _ in range(N)]
seen[Ax - 1][Ay - 1] = True
ans = 0

def dfs(tmpx, tmpy, idx, ans, seen):
    seen[tmpx][tmpy] = True
    if (tmpx, tmpy) == (Bx - 1, By - 1):
        return True
    for i in range(4):
        i = (idx + i) % 4
        nx = tmpx + d[i][0]
        ny = tmpy + d[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            if (S[nx][ny] == '.') and (not seen[nx][ny]):
                if idx != i:
                    ans += 1
                dfs(nx, ny, idx, ans, seen)
                
print(dfs(Ax - 1, Ay - 1, 0, ans, seen))