import functools
import sys

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


def read():
    return list(map(int, input().strip().split()))


def solve(l, k, d, a):
    d.append(l)

    @functools.lru_cache(maxsize=None)
    def solve_rec(position, drops, speed):
        if position >= len(a):
            return 0
        res = MAX
        if drops > 0 and a[position] > speed:
            res = min(res, speed * (d[position + 1] - d[position]) + solve_rec(position + 1, drops - 1, speed))
        res = min(res, a[position] * (d[position + 1] - d[position]) + solve_rec(position + 1, drops, a[position]))
        return res

    return solve_rec(0, k, a[0])


if __name__ == "__main__":
    n, l, k = read()
    d = read()
    a = read()

    print(solve(l, k, d, a))
