# https://codeforces.com/problemset/problem/1627/B

import sys

input = sys.stdin.readline
MAX = sys.maxsize

sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def read_list():
    s = input()
    return list(s[:len(s) - 1])


# Solution
def manhattan(x, y, a, b):
    return abs(x - a) + abs(y - b)


def solve(n, m):
    corners = [(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)]
    d = []
    for x in range(n):
        for y in range(m):
            cd = []
            for c in corners:
                cd.append(manhattan(x, y, c[0], c[1]))
            d.append(max(cd))
    print(*sorted(d))


if __name__ == "__main__":
    for _ in range(inp()):
        n, m = read_int_list()
        solve(n, m)
