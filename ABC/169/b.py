n = int(input())
a = list(map(int, input().split()))  # 入力受け取り
a.sort()  # 小さい順にする
ans = 1
INF = 10 ** 18
for i in a:
    ans *= i
    if ans == 0:  # 0になったらその時点で答え0なのでやめる
        print(0)
        break
    elif ans > INF:  # INFを超えてもそのあとは無駄なのでやめる
        print(-1)
        break
else:  # for文が終わったら答えをそのまま出力する
    if ans > INF:
        print(-1)
    else:
        print(ans)
