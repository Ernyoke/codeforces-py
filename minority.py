# https://codeforces.com/problemset/problem/1633/B

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


def read_int_map():
    return map(int, input().split())


# Solution
def solve(st):
    zeros, ones = 0, 0
    for c in st:
        if c == '0':
            zeros += 1
        else:
            ones += 1

    if zeros == ones:
        return zeros - 1
    elif zeros < ones:
        return zeros
    return ones


if __name__ == "__main__":
    for _ in range(inp()):
        st = read_list()
        print(solve(st))
