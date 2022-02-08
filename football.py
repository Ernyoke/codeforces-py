# https://codeforces.com/problemset/problem/96/A

import sys
from itertools import groupby

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
def solve(players):
    for key, value in groupby(players):
        if len(list(value)) >= 7:
            return "YES"
    return "NO"


if __name__ == "__main__":
    print(solve(read_list()))
