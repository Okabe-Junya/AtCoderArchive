K = int(input())
if K >= 60:
    k60 =str(K - 60).zfill(2)
    print("22:{}".format(k60))
else:
    print("21:{}".format(str(K).zfill(2)))