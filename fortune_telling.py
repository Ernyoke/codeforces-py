# https://codeforces.com/problemset/problem/1634/B

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
def solve(x, y, a):
    if sum(a) % 2 == (x - y) % 2:
        return "Alice"
    return "Bob"


if __name__ == "__main__":
    for _ in range(inp()):
        n, x, y = read_int_list()
        a = read_int_list()
        print(solve(x, y, a))