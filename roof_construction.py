# https://codeforces.com/problemset/problem/1632/B

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
def solve(n):
    x = 1
    while x < n:
        x <<= 1
    rev = x >> 1
    for i in range(rev - 1, -1, -1):
        print(f'{i} ', end='')
    for i in range(rev, n):
        print(f'{i} ', end='')
    print()


if __name__ == "__main__":
    for _ in range(inp()):
        solve(inp())
