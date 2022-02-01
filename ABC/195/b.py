a, b, w = map(int, input().split())
mi = 1000 * w // b
ma = 1000 * w // a
if 1000 * w - a * ma > (b-a) * ma:
    print('UNSATISFIABLE ')
else:
    if (1000 * w) % b != 0:
        mi += 1
    print(mi, ma)
