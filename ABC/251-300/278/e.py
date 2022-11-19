H, W, N, h, w = map(int, input().split())
Al = []
ts = set()
for i in range(H):
    A = list(map(int, input().split()))
    Al.append(A)
    for j in range(W):
        ts.add(A[j])
all_num = len(ts)
place = {}
for i in range(H):
    for j in range(W):
        if Al[i][j] not in place:
            place[Al[i][j]] = {"left": j, "right": j, "top": i, "bottom": i}
        else:
            place[Al[i][j]]["left"] = min(place[Al[i][j]]["left"], j)
            place[Al[i][j]]["right"] = max(place[Al[i][j]]["right"], j)
            place[Al[i][j]]["top"] = min(place[Al[i][j]]["top"], i)
            place[Al[i][j]]["bottom"] = max(place[Al[i][j]]["bottom"], i)

ans_list = [[-1 for i in range(W - w + 1)] for j in range(H - h + 1)]
for i in range(H - h + 1):
    for j in range(W - w + 1):
        cnt = 0
        for k in place:
            if ((i <= place[k]["top"]) and (i + h - 1 >= place[k]["bottom"]) and (j <= place[k]["left"]) and (j + w - 1 >= place[k]["right"])):
                cnt += 1
        ans_list[i][j] = all_num - cnt


for i in range(H - h + 1):
    print(*ans_list[i])
