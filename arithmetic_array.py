# https://codeforces.com/problemset/problem/1537/A

import sys

input = sys.stdin.readline


def read_int_list():
    return list(map(int, input().split()))


def solve(a):
    s, n = sum(a), len(a)
    if s >= 0 and s - n >= 0:
        return s - n
    return 1


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(solve(read_int_list()))
