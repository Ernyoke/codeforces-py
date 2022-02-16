# https://codeforces.com/problemset/problem/1637/C

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
    if len(a) == 3:
        if a[1] % 2 == 1:
            return -1
    mid = a[1:-1]
    if all([value == 1 for value in mid]):
        return -1
    return sum([(value + 1) // 2 for value in mid])


if __name__ == "__main__":
    for _ in range(inp()):
        _ = inp()
        print(solve(read_int_list()))
