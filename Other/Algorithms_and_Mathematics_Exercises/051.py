from scipy.special import comb

x, y = map(int, input().split())
INF = 10 ** 9 + 7
print(comb(x + y, x, exact=True) % INF)