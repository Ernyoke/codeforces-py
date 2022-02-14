# https://codeforces.com/problemset/problem/1637/B

import sys
from itertools import combinations

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
def sub_segments(a):
    return [(a[x:y]) for x, y in combinations(range(len(a) + 1), r=2)]


def compute(a):
    zeros = 0
    for value in a:
        if value == 0:
            zeros += 1
    return len(a) + zeros


def solve(a):
    return sum([compute(s) for s in sub_segments(a)])


if __name__ == "__main__":
    for _ in range(inp()):
        _ = inp()
        print(solve(read_int_list()))
