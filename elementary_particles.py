# https://codeforces.com/problemset/problem/1625/B

import sys

input = sys.stdin.readline
MAX = sys.maxsize

# sys.setrecursionlimit(10 ** 9)


# Input functions
def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def read_list():
    s = input()
    return list(s[:len(s) - 1])


def read_int_map():
    return map(int, input().split())


# Solution
def solve(a):
    d = dict()
    for i, value in enumerate(a):
        d.setdefault(value, []).append(i + 1)

    ans = -1
    for positions in d.values():
        if len(positions) >= 2:
            for i in range(0, len(positions) - 1):
                ans = max(ans, len(a) - (positions[i + 1] - positions[i]))

    return ans


if __name__ == "__main__":
    for _ in range(inp()):
        _ = inp()
        print(solve(read_int_list()))
