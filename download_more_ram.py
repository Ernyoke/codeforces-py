# https://codeforces.com/problemset/problem/1629/A

import sys

input = sys.stdin.readline


def inp():
    return int(input())


def read_int_list():
    return list(map(int, input().split()))


def solve(a, b, k):
    zipped = list(reversed(sorted(zip(a, b))))
    available = k
    while zipped:
        prog, additional = zipped.pop()
        if prog <= available:
            available += additional
        else:
            break
    return available


if __name__ == "__main__":
    for _ in range(inp()):
        n, k = read_int_list()
        a = read_int_list()
        b = read_int_list()
        print(solve(a, b, k))
