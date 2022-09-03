from itertools import combinations as cmb

S = input()
if S[0] == '1':
    print("No")
    exit()

L = {1: 3, 2: 2, 3: 4, 4: 1, 5: 3, 6: 5, 7: 0, 8: 2, 9: 4, 10: 6}

cnt = [0] * 7
for i in range(10):
    if S[i] == '1':
        cnt[L[i + 1]] += 1

for i in cmb(range(7), 3):
    if cnt[i[0]] and cnt[i[2]] and (not cnt[i[1]]):
        print('Yes')
        exit()
else:
    print('No')

