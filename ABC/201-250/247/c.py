N = int(input())


def solve(n, string):
    if n == 0:
        return string
    return solve(n - 1, string) + " " + str(n) + " " + solve(n - 1, string)


tmp = solve(N, "")
tmp.replace("  ", " ")
print(tmp.strip())
