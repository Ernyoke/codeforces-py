# https://codeforces.com/problemset/problem/1637/A

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
def solve(a):
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            return "YES"
    return "NO"


if __name__ == "__main__":
    for _ in range(inp()):
        _ = inp()
        print(solve(read_int_list()))
